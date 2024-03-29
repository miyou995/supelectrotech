# Generated by Django 3.1.3 on 2020-12-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201129_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ['ordre'], 'verbose_name': 'Produits', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AddField(
            model_name='produit',
            name='ordre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='fichier_1',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='Fiche technique '),
        ),
        migrations.AlterField(
            model_name='produit',
            name='fichier_2',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='Manuel instalateur'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='fichier_3',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='Manuel utilisateur'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='fichier_4',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='certificat'),
        ),
    ]
