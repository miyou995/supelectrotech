# Generated by Django 3.1.3 on 2020-11-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201125_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='photo_2',
        ),
        migrations.AlterField(
            model_name='produit',
            name='fichier_1',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='Catalogue'),
        ),
    ]