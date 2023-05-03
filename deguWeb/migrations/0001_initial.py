# Generated by Django 4.1.3 on 2023-03-23 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BiGG",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="CAZy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Clade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eggdbId", models.IntegerField()),
                ("cladeValue", models.CharField(max_length=250)),
                (
                    "parentId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.clade"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cld", models.CharField(blank=True, max_length=50)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="COG",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=50)),
                ("letter", models.CharField(max_length=1)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="EC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ecValue", models.CharField(max_length=50)),
                (
                    "parentId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.ec"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EggNOGOG",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(default="default", max_length=50)),
                (
                    "cladeId",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.clade",
                    ),
                ),
                (
                    "parentId",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.eggnogog",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genbank", models.CharField(max_length=50)),
                ("length", models.IntegerField()),
                ("annotated", models.BooleanField()),
                ("seedOrtholog", models.CharField(max_length=50)),
                ("evalueEggnog", models.FloatField()),
                ("scoreEggnog", models.FloatField()),
                ("description", models.CharField(max_length=50)),
                ("preferredName", models.CharField(default="", max_length=250)),
                (
                    "clusterId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.cluster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GenomeVersion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("ncbi_link", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="GO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("go", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGBRITE",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGKO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGPathway",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGrclass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGReaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="KEGGTC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PFAM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("userrole", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Specie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("commonName", models.CharField(max_length=50)),
                ("code", models.CharField(default="default", max_length=50)),
                ("specie", models.CharField(max_length=50)),
                ("genre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("usertype", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=250)),
                ("password", models.CharField(max_length=15)),
                ("name", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("image", models.CharField(max_length=250)),
                ("team", models.IntegerField()),
                (
                    "roleId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.role"
                    ),
                ),
                (
                    "typeId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PFAMGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "pfamId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.pfam"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGTCGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "tcId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.keggtc"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGReactionGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "reactionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.keggreaction",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGrclassGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "rclassId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.keggrclass",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGPathwayGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "pathwayId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.keggpathway",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGModuleGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "moduleId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.keggmodule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGKOGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "koId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.keggko"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KEGGBRITEGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "briteId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.keggbrite",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GOParentChild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gochildId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child",
                        to="deguWeb.go",
                    ),
                ),
                (
                    "goparentId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parent",
                        to="deguWeb.go",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GOGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "goId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.go"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GenomeVersionGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "genomeversionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.genomeversion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="genomeversion",
            name="specieId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="deguWeb.specie"
            ),
        ),
        migrations.CreateModel(
            name="EggNOGOGGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "eggnogogId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.eggnogog",
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ECGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ecId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.ec"
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="COGGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cogId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.cog"
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClusterSpecie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "clusterId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.cluster",
                    ),
                ),
                (
                    "specieId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.specie"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CAZyGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cazyId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.cazy"
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BiGGGene",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "biggId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.bigg"
                    ),
                ),
                (
                    "geneId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
    ]
