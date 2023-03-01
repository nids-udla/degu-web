# Generated by Django 4.1.3 on 2023-02-20 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("deguWeb", "0004_bigg_cog_ec_gene_goparentchild_gogene_and_more"),
    ]

    operations = [
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
        migrations.RenameField(
            model_name="ec", old_name="enzymecomission", new_name="ecValue",
        ),
        migrations.RemoveField(model_name="eggnogog", name="eggnogogId",),
        migrations.RemoveField(model_name="eggnogog", name="ensembl",),
        migrations.AddField(
            model_name="cluster",
            name="cld",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="eggnogog",
            name="parentId",
            field=models.ForeignKey(
                default="000",
                on_delete=django.db.models.deletion.CASCADE,
                to="deguWeb.eggnogog",
            ),
        ),
        migrations.AddField(
            model_name="gene",
            name="preferredName",
            field=models.CharField(default="", max_length=250),
        ),
        migrations.AlterField(
            model_name="genomeversiongene",
            name="genomeversionId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="deguWeb.genomeversion"
            ),
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
        migrations.AddField(
            model_name="eggnogog",
            name="cladeId",
            field=models.ForeignKey(
                default="000",
                on_delete=django.db.models.deletion.CASCADE,
                to="deguWeb.clade",
            ),
        ),
    ]