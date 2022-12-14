# Generated by Django 4.1.2 on 2022-11-02 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("titulo", models.CharField(max_length=128)),
                ("fecha_registro", models.DateField()),
                ("cant_registrada", models.IntegerField()),
                ("cant_actual", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("nombre", models.CharField(max_length=50)),
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("rol", models.IntegerField()),
                ("cant_max", models.IntegerField()),
                ("prestamos_actuales", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Registro",
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
                ("tipo", models.BooleanField()),
                ("cantidad", models.IntegerField()),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="biblioteca.material",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="biblioteca.usuario",
                    ),
                ),
            ],
        ),
    ]
