# Generated by Django 3.1.3 on 2020-12-21 09:19

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20201220_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Categories des articles'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='created_month',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_1',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='text 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_2',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='text 2'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_3',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='text 3'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tag', verbose_name='Categorie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=50, verbose_name='categorie'),
        ),
    ]