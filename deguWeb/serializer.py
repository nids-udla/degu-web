from rest_framework import serializers
from .models import Type, Role, Users, Specie, Cluster, ClusterSpecie, Gene, GenomeVersion, GenomeVersionGene, GO, GOGene, GOParentChild, COG, COGGene, Clade, EggNOGOG, EggNOGOGGene, BiGG, BiGGGene, EC, ECGene, KEGGKO, KEGGKOGene, KEGGModule, KEGGModuleGene, KEGGPathway, KEGGPathwayGene, KEGGReaction, KEGGReactionGene, KEGGrclass, KEGGrclassGene, KEGGBRITE, KEGGBRITEGene, KEGGTC, KEGGTCGene, PFAM, PFAMGene, CAZy, CAZyGene

# There is a serializer to every class in models.py except for the intermediate tables.

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('usertype')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('userrole')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'password', 'name', 'lastName', 'image', 'team')

class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ('commonName', 'code', 'specie', 'genre')

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = ('cld', 'description')

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ('genbank', 'length', 'annotated', 'seedOrtholog', 'evalueEggnog', 'scoreEggnog', 'description', 'preferredName')

class GenomeVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeVersion
        fields = ('name', 'ncbi_link')

class GOSerializer(serializers.ModelSerializer):
    class Meta:
        model = GO
        fields = ('go', 'description')

class GOParentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOParentChild
        fields = ('goparentId', 'gochildId')

class COGSerializer(serializers.ModelSerializer):
    class Meta:
        model = COG
        fields = ('color', 'letter', 'description')

class CladeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clade
        fields = ('eggdbId', 'cladeValue')

class EggNOGOGSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggNOGOG
        fields = ('code')

class BiGGSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiGG
        fields = ('model', 'description')

class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = EC
        fields = ('ecValue', 'parentId')

class KEGGKOSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGKO
        fields = ('name')

class KEGGModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGModule
        fields = ('name')

class KEGGPathwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGPathway
        fields = ('name')

class KEGGReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGReaction
        fields = ('name')

class KEGGrclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGrclass
        fields = ('name')

class KEGGBRITESerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGBRITE
        fields = ('name')

class KEGGTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KEGGTC
        fields = ('name')

class PFAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = PFAM
        fields = ('name')

class CAZySerializer(serializers.ModelSerializer):
    class Meta:
        model = CAZy
        fields = ('name')