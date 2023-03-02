# Generated by Django 4.1.7 on 2023-03-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=250)),
                ("subtitle", models.CharField(max_length=250)),
                ("author", models.CharField(max_length=250)),
                ("isbn", models.CharField(max_length=13)),
            ],
        ),
    ]