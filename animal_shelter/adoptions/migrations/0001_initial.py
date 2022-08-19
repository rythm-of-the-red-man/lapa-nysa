# Generated by Django 4.1 on 2022-08-09 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
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
                ("created_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50, verbose_name="Imię")),
                (
                    "spice",
                    models.CharField(
                        choices=[("Pies", "Pies"), ("Kot", "Kot"), ("Inne", "Inne")],
                        max_length=50,
                        verbose_name="Gatunek",
                    ),
                ),
                ("description", models.TextField(verbose_name="Opis")),
                ("age", models.IntegerField(verbose_name="Wiek")),
                ("weight", models.FloatField(verbose_name="Waga")),
                ("additional_notes", models.TextField(verbose_name="Dodatkowe uwagi")),
                (
                    "sex",
                    models.CharField(
                        choices=[("Samiec", "Samiec"), ("Samica", "Samica")],
                        max_length=50,
                        verbose_name="Płeć",
                    ),
                ),
                (
                    "breed",
                    models.CharField(max_length=100, verbose_name="Rasa / W typie..."),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("Mały zwierzak", "Mały zwierzak"),
                            ("Średni zwierzak", "Średni zwierzak"),
                            ("Duzy zwierzak", "Duzy zwierzak"),
                        ],
                        max_length=50,
                        verbose_name="Rozmiar",
                    ),
                ),
            ],
            options={
                "verbose_name": "Zwierzę",
                "verbose_name_plural": "Zwierzęta",
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("created_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50, verbose_name="Imię")),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="Numer kontaktowy"),
                ),
            ],
            options={
                "verbose_name": "Kontakt",
                "verbose_name_plural": "Kontakty",
            },
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("created_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="", verbose_name="Zdjęcie")),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="adoptions.animal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Zdjęcie",
                "verbose_name_plural": "Zdjęcia",
            },
        ),
        migrations.AddField(
            model_name="animal",
            name="contacts",
            field=models.ManyToManyField(
                to="adoptions.contact", verbose_name="Numery kontaktowe do adopcji"
            ),
        ),
    ]
