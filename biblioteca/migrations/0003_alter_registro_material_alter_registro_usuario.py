# Generated by Django 4.1.2 on 2022-11-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0002_alter_registro_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registro",
            name="material",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="registro",
            name="usuario",
            field=models.CharField(max_length=50),
        ),
    ]
