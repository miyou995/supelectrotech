# Generated by Django 3.1.3 on 2020-12-08 07:11

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201208_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('ordre'), nulls_last=True)], 'verbose_name': 'Produits', 'verbose_name_plural': 'Produits'},
        ),
    ]
