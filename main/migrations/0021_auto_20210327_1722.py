# Generated by Django 3.1.3 on 2021-03-27 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_catalogue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='Nom',
            new_name='nom',
        ),
    ]
