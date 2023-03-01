from django.db import models

# Create your models here.
#------------------------------------------------------------
# Orden de tablas:
    # Type
    # Role
    # Users

    # Specie
    # Cluster
    # ClusterSpecie
    # Gene
    # GenomeVersion
    # GenomeVersionGene

    # GO
    # GOGene
    # GOParentChild
    # COG
    # COGGENE
    # Clade
    # EggNOGOG
    # EggNOGOGGene
    # BiGG
    # BiGGGene
    # EC
    # ECGene
    # KEGGKO
    # KEGGKOGene
    # KEGGModule
    # KEGGModuleGene
    # KEGGPathway
    # KEGGPathwayGene
    # KEGGReaction
    # KEGGReactionGene
    # KEGGrclass
    # KEGGrclassGene
    # KEGGBRITE
    # KEGGBRITEGene
    # KEGGTC
    # KEGGTCGene
    # PFAM
    # PFAMGene
    # CAZy
    # CAZyGene
#------------------------------------------------------------
#------------------------------------------------------------

class Type(models.Model):
    usertype = models.CharField(max_length=250)

    def __str__(self):
        return 'Type: {}'.format(self.usertype)

class Role(models.Model):
    userrole = models.CharField(max_length=250)

    def __str__(self):
        return 'Role: {}'.format(self.userrole)

class Users(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    team = models.IntegerField()
    typeId = models.ForeignKey(Type, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return 'Name: {} LastName: {} Password: {} Team: {} Type: {} Role: {}'.format(self.name,self.lastName,self.password,self.team,self.typeId,self.roleType)
#------------------------------------------------------------
#------------------------------------------------------------

class Specie(models.Model):
    commonName = models.CharField(max_length=50)
    code = models.CharField(max_length=50, default='default')
    specie = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {} code: {} Specie: {} Genre: {}'.format(self.commonName,self.code,self.specie,self.genre)

class Cluster(models.Model):
    cld = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return 'Description: {} CLD: {}'.format(self.description,self.cld)

class ClusterSpecie(models.Model):
    specieId = models.ForeignKey(Specie, on_delete=models.CASCADE)
    clusterId = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return 'SpecieId: {} ClusterId: {}'.format(self.specieId,self.clusterId)

class Gene(models.Model):
    genbank = models.CharField(max_length=50)
    length = models.IntegerField()
    annotated = models.BooleanField()
    seedOrtholog = models.CharField(max_length=50)
    evalueEggnog = models.FloatField()
    scoreEggnog = models.FloatField()
    description = models.CharField(max_length=50)
    preferredName = models.CharField(max_length=250, default='')
    clusterId = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return 'GenBank: {} Description: {} ClusterId: {} Preferred Name: {}'.format(self.genbank,self.description,self.clusterId,self.preferredName)

class GenomeVersion(models.Model):
    specieId = models.ForeignKey(Specie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ncbi_link = models.CharField(max_length=50)

    def __str__(self):
        return 'SpecieId: {} Name: {} Ncbi_link: {}'.format(self.specieId,self.name,self.ncbi_link)

class GenomeVersionGene(models.Model):
    genomeversionId = models.ForeignKey(GenomeVersion, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'GenomeVersionId: {} GeneId: {}'.format(self.genomeversionId,self.geneId)
#------------------------------------------------------------
#------------------------------------------------------------

class GO(models.Model):
    go = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return 'GO: {} Description: {}'.format(self.go,self.description)

class GOGene(models.Model):
    goId = models.ForeignKey(GO, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'GOId: {} GeneId: {}'.format(self.goId,self.geneId)

class GOParentChild(models.Model):
    goparentId = models.ForeignKey(GO, on_delete=models.CASCADE, related_name='parent')
    gochildId = models.ForeignKey(GO, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return 'ParentId: {} ChildId: {}'.format(self.goparentId,self.gochildId)

class COG(models.Model):
    color = models.CharField(max_length=50)
    letter = models.CharField(max_length=1)
    description = models.CharField(max_length=250)

    def __str__(self):
        return 'Color: {} Letter: {} Description: {}'.format(self.color,self.letter,self.description)

class COGGene(models.Model):
    cogId = models.ForeignKey(COG, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'COGId: {} GeneId: {}'.format(self.cogId,self.geneId)

class Clade(models.Model):
    eggdbId = models.IntegerField()
    cladeValue = models.CharField(max_length=250)
    parentId = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return 'EggdbId: {} Clade: {} parentId: {}'.format(self.eggdbId,self.cladeValue,self.parentId)

class EggNOGOG(models.Model):
    code = models.CharField(max_length=50, default='default')
    parentId = models.ForeignKey('self', on_delete=models.CASCADE, default='')
    cladeId = models.ForeignKey(Clade, on_delete=models.CASCADE, default='')

    def __str__(self):
        return 'Code: {} parentId: {} CladeId: {}'.format(self.code,self.parentId,self.cladeId)

class EggNOGOGGene(models.Model):
    eggnogogId = models.ForeignKey(EggNOGOG, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'EggnogogId: {} GeneId: {}'.format(self.eggnogogId,self.geneId)

class BiGG(models.Model):
    model = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return 'Model: {} Description: {}'.format(self.model,self.description)

class BiGGGene(models.Model):
    biggId = models.ForeignKey(BiGG, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'BiGGId: {} GeneId: {}'.format(self.biggId,self.geneId)

class EC(models.Model):
    ecValue = models.CharField(max_length=50)
    parentId = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return 'EC: {} ParentId: {}'.format(self.ecValue,self.parentId)

class ECGene(models.Model):
    ecId = models.ForeignKey(EC, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'ECId: {} GeneId: {}'.format(self.ecId,self.geneId)

class KEGGKO(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGKOGene(models.Model):
    koId = models.ForeignKey(KEGGKO, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'KOId: {} GeneId: {}'.format(self.koId,self.geneId)

class KEGGModule(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGModuleGene(models.Model):
    moduleId = models.ForeignKey(KEGGModule, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'ModuleId: {} GeneId: {}'.format(self.moduleId,self.geneId)

class KEGGPathway(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGPathwayGene(models.Model):
    pathwayId = models.ForeignKey(KEGGPathway, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'PathwayId: {} GeneId: {}'.format(self.pathwayId,self.geneId)

class KEGGReaction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGReactionGene(models.Model):
    reactionId = models.ForeignKey(KEGGReaction, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'ReactionId: {} GeneId: {}'.format(self.reactionId,self.geneId)

class KEGGrclass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGrclassGene(models.Model):
    rclassId = models.ForeignKey(KEGGrclass, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'RclassId: {} GeneId: {}'.format(self.rclassId,self.geneId)

class KEGGBRITE(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGBRITEGene(models.Model):
    briteId = models.ForeignKey(KEGGBRITE, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'BriteId: {} GeneId: {}'.format(self.briteId,self.geneId)

class KEGGTC(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class KEGGTCGene(models.Model):
    tcId = models.ForeignKey(KEGGTC, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'TcId: {} GeneId: {}'.format(self.tcId,self.geneId)

class PFAM(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class PFAMGene(models.Model):
    pfamId = models.ForeignKey(PFAM, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'PfamId: {} GeneId: {}'.format(self.pfamId,self.geneId)

class CAZy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class CAZyGene(models.Model):
    cazyId = models.ForeignKey(CAZy, on_delete=models.CASCADE)
    geneId = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return 'CazyId: {} GeneId: {}'.format(self.cazyId,self.geneId)