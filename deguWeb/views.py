# ---------- The form ----------
from .forms import Filter
# ---------- To visualize ----------
from rpy2 import robjects
# ---------- To Users ----------
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_process
from django.contrib.auth import logout as logout_process
# ---------- To render the info ----------
from django.shortcuts import redirect, render
from .models import Type, Role, Users, Specie, Cluster, Gene, GenomeVersion, GenomeVersionGene, GO, GOGene, GOParentChild, COG, COGGene, Clade, EggNOGOG, EggNOGOGGene, BiGG, BiGGGene, EC, ECGene, KEGGKO, KEGGKOGene, KEGGModule, KEGGModuleGene, KEGGPathway, KEGGPathwayGene, KEGGReaction, KEGGReactionGene, KEGGrclass, KEGGrclassGene, KEGGBRITE, KEGGBRITEGene, KEGGTC, KEGGTCGene, PFAM, PFAMGene, CAZy, CAZyGene
# ---------- To download the info ----------
import pandas as pd
from openpyxl import Workbook
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def login(request):

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login_process(request, user)

            return render(request, 'search.html')
        else:
            return redirect('/')

    return render(request, 'login.html')

def logout(request):

    logout_process(request)

    return render(request, 'home.html')

def search(request):

    return render(request, 'search.html')

def filter(request):
    # --- Initializing some variables ---
    toSearch = []
    genes = []
    k = 0
  
    # --- Adding the checked boxes to compare against the db ---
    if request.POST:
        if request.POST.get('hs') == 'on':
            toSearch.append('hs')
        if request.POST.get('od') == 'on':
            toSearch.append('od')
        if request.POST.get('mm') == 'on':
            toSearch.append('mm')
        if request.POST.get('hg') == 'on':
            toSearch.append('hg')

    # --- Searching for the cluster id ---
    groups = Cluster.objects.all()
    for e in groups:
        if str(e.description).split(',') == toSearch:
            # --- Using cluster id to filter the genes ---
            k = e.id
            genes = Gene.objects.filter(clusterId=k)
            # --- Saving cluster id in a session ---
            request.session['key'] = k
            break
        else:
            genes = []
            
    return render(request, 'search.html', {
        'genes':genes,
    })

def download(request):
    # --- Using cluster id to filter the genes ---
    k = request.session.get('key')
    genes = Gene.objects.filter(clusterId=k)

    # --- Creating excel with pandas ---
    df = pd.DataFrame(list(genes.values()))
    writer = pd.ExcelWriter('excel/genes.xlsx')
    df.to_excel(writer)

    writer.save()

    # --- Downloading the excel ---
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'genes.xlsx'
    filepath = base_dir + '/excel/' + filename
    theFile = filepath
    filename = os.path.basename(theFile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(theFile,'rb'),chunk_size),content_type=mimetypes.guess_type(theFile)[0])
    response['Content-Length'] = os.path.getsize(theFile)
    response['Content-Disposition'] = 'Attachment;filename={}'.format(filename)

    return response

def extended(request):
    genes = []

    # --- Using cluster id to filter the genes ---
    k = request.session.get('key')
    genes = Gene.objects.filter(cluster=k)

    # --- Calling R script ---
    robjects.r('''
    library(pathview)

    genes <- read.delim('genes/{}.txt', header = F)

    pv.out <- pathview(gene.data = genes, pathway.id = '05010', species = 'ko ', kegg.native = T, same.layer = T, out.suffix = 'deguweb', gene.idtype = 'genbank', sign.pos = 'right')
    '''.format(specie))
    return render(request, 'extended.html')