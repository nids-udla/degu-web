from django.contrib import admin
from .models import SPECIE, CLUSTER, GENOMEVERSION, GENE, GENOMEVERSION_GENE, COG, COG_GENE, EC, EC_GENE, EGGNOG_OG, EGGNOGOGGENE_GENE, GENONTOLOGY, GENONTOLOGY_GEN, CLUSTER

# Register your models here.
admin.site.register(SPECIE)
admin.site.register(GENOMEVERSION)
admin.site.register(GENE)
admin.site.register(GENOMEVERSION_GENE)
admin.site.register(COG)
admin.site.register(COG_GENE)
admin.site.register(EC)
admin.site.register(EC_GENE)
admin.site.register(EGGNOG_OG)
admin.site.register(EGGNOGOGGENE_GENE)
admin.site.register(GENONTOLOGY)
admin.site.register(GENONTOLOGY_GEN)
admin.site.register(CLUSTER)