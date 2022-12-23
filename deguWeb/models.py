from django.db import models

# Create your models here.
# *LAS TABLAS INTERMEDIAS NO DEVUELVEN INFO AL ADMIN
#------------------------------------------------------------
# Orden de tablas:
#   - SPECIE
#   - CLUSTER
#   - GENOMEVERSION
#   - GENE
#   - GENOMEVERSION_GENE
#   - COG
#   - COG_GENE
#   - EC
#   - EC_GENE
#   - EGGNOG_OG
#   - EGGNOGOGGENE_GENE
#   - GENONTOLOGY
#   - GENONTOLOGY_GEN
#------------------------------------------------------------
# Pendientes:
#   - BIGG
#   - BIGG_GENE
#------------------------------------------------------------

class SPECIE(models.Model):
    commonName = models.CharField(max_length=50)
    specie = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: {} Specie: {} Genre: {}'.format(self.commonName,self.specie,self.genre)

class CLUSTER(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return('Name: {} // Description: {}'.format(self.name,self.description))

class GENOMEVERSION(models.Model):
    name = models.CharField(max_length=50)
    ncbi_link = models.CharField(max_length=50)
    id_specie = models.ForeignKey(SPECIE, on_delete=models.CASCADE)

    def __str__(self):
        return 'Name: {} NCBI: {}'.format(self.name,self.ncbi_link)

class GENE(models.Model):
    genbank = models.CharField(max_length=50)
    length = models.IntegerField()
    annotated = models.BooleanField() # Pedir valores predeterminados
    seed_ortholog = models.CharField(max_length=50)
    evalue_eggnog = models.FloatField() # Pedir valores predeterminados
    score_eggnog = models.FloatField() # Pedir valores predeterminados
    description = models.CharField(max_length=250)
    cluster = models.ForeignKey(CLUSTER, on_delete=models.CASCADE)

    def __str__(self):
        return 'GenBank: {} Length: {} Annotated: {} Seed Ortholog: {} Evalue Eggnog: {} Score Eggnog: {} Description: {}'.format(self.genbank,self.length,self.annotated,self.seed_ortholog,self.evalue_eggnog,self.score_eggnog,self.description)

class GENOMEVERSION_GENE(models.Model):
    id_gene = models.ForeignKey(GENE, on_delete=models.CASCADE)
    id_genomeversion= models.ForeignKey(GENOMEVERSION, on_delete=models.CASCADE)

class COG(models.Model):
    color = models.CharField(max_length=50)
    cogletter = models.CharField(max_length=1)
    description = models.CharField(max_length=150)

    def __str__(self):
        return 'Color: {} Cogletter: {} Description: {}'.format(self.color,self.cogletter,self.description)

class COG_GENE(models.Model):
    id_gene = models.ForeignKey(GENE, on_delete=models.CASCADE)
    id_cog = models.ForeignKey(COG, on_delete=models.CASCADE)

class EC(models.Model):
    test = models.CharField(max_length=50)
    brenda_link = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    id_EC = models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
        return 'EC: {} Brenda Link: {} Description: {} Parent: {}'.format(self.ec,self.brenda_link,self.description,self.id_EC)

class EC_GENE(models.Model):
    id_gene = models.ForeignKey(GENE,on_delete=models.CASCADE)
    id_ec = models.ForeignKey(EC,on_delete=models.CASCADE)

class EGGNOG_OG(models.Model):
    code = models.CharField(max_length=50)
    ensembl = models.CharField(max_length=50)
    id_eggnogoggene = models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
        return 'Code: {} Ensembl: {} Parent: {}'.format(self.code,self.ensembl,self.id_eggnogoggene)

class EGGNOGOGGENE_GENE(models.Model):
    id_gene = models.ForeignKey(GENE,on_delete=models.CASCADE)
    id_eggnogoggene = models.ForeignKey(EGGNOG_OG,on_delete=models.CASCADE)

class GENONTOLOGY(models.Model):
    go = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    id_genontology = models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
        return 'Geneontology: {} Description: {} Parent: {}'.format(self.go,self.description,self.id_genontology)

class GENONTOLOGY_GEN(models.Model):
    id_gene = models.ForeignKey(GENE,on_delete=models.CASCADE)
    id_geneontology = models.ForeignKey(GENONTOLOGY,on_delete=models.CASCADE)

