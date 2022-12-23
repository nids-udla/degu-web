# ---------- The form ----------
from .forms import Filter
# ---------- The tables ----------
from .models import SPECIE, CLUSTER, GENOMEVERSION, GENE, GENOMEVERSION_GENE, COG, COG_GENE, EC, EC_GENE, EGGNOG_OG, EGGNOGOGGENE_GENE, GENONTOLOGY, GENONTOLOGY_GEN, CLUSTER
# ---------- To render the info ----------
from django.shortcuts import render
# from .models import gen, attribute, SPECIE, group
# ---------- To download the info ----------
import pandas as pd
from openpyxl import Workbook
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

# Create your views here.
def home(request):
    # --- Initializing some variables ---
    toSearch = []
    genes = []
    k = 0

    # --- Adding the checked boxes to compare against the db ---
    if request.POST:
        if request.POST.get('specie_sapiens') == 'on':
            toSearch.append('hs')
        if request.POST.get('specie_degu') == 'on':
            toSearch.append('od')
        if request.POST.get('specie_rat') == 'on':
            toSearch.append('mm')
        if request.POST.get('specie_nmr') == 'on':
            toSearch.append('nmr')

    # --- Searching for the cluster id ---
    groups = CLUSTER.objects.all()
    for e in groups:
        if str(e.description).split(',') == toSearch:
            # --- Using cluster id to filter the genes ---
            k = e.id
            genes = GENE.objects.filter(cluster=k)
            # --- Saving cluster id in a session ---
            request.session['key'] = k
            break
        else:
            genes = []
            
    return render(request, 'home.html', {
        'filter':Filter(),
        'genes':genes,
    })

def download(request):
    # --- Using cluster id to filter the genes ---
    k = request.session['key']
    genes = GENE.objects.filter(cluster=k)

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