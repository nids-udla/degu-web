# Generated by Django 4.1.3 on 2022-12-21 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CLUSTER",
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
                ("cogletter", models.CharField(max_length=1)),
                ("description", models.CharField(max_length=150)),
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
                ("test", models.CharField(max_length=50)),
                ("brenda_link", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=150)),
                (
                    "id_EC",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.ec"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EGGNOG_OG",
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
                ("code", models.CharField(max_length=50)),
                ("ensembl", models.CharField(max_length=50)),
                (
                    "id_eggnogoggene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.eggnog_og",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GENE",
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
                ("seed_ortholog", models.CharField(max_length=50)),
                ("evalue_eggnog", models.FloatField()),
                ("score_eggnog", models.FloatField()),
                ("description", models.CharField(max_length=250)),
                (
                    "cluster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.cluster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GENOMEVERSION",
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
            name="GENONTOLOGY",
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
                (
                    "id_genontology",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.genontology",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SPECIE",
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
                ("specie", models.CharField(max_length=50)),
                ("genre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="GENONTOLOGY_GEN",
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
                    "id_gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "id_geneontology",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.genontology",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GENOMEVERSION_GENE",
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
                    "id_gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
                (
                    "id_genomeversion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.genomeversion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="genomeversion",
            name="id_specie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="deguWeb.specie"
            ),
        ),
        migrations.CreateModel(
            name="EGGNOGOGGENE_GENE",
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
                    "id_eggnogoggene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deguWeb.eggnog_og",
                    ),
                ),
                (
                    "id_gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EC_GENE",
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
                    "id_ec",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.ec"
                    ),
                ),
                (
                    "id_gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="COG_GENE",
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
                    "id_cog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.cog"
                    ),
                ),
                (
                    "id_gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="deguWeb.gene"
                    ),
                ),
            ],
        ),
    ]