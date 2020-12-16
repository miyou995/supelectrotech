from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import F

from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
# Create your models here.

CATEGORY_CHOICES=[
    ('IN', 'Intrusion'),
    ('IC', 'Incendie Conventionnelle'),
    ('IA', 'Incendie Adressable'),
    ]


class Produit(models.Model):
    ordre           = models.IntegerField(blank=True, null=True )
    designation     = models.CharField( max_length=150, verbose_name=("Désignation"))
    slug            = models.SlugField( max_length=70)
    category        = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='IN')
    reference       = models.CharField(max_length=100, verbose_name=("Référence"), blank= True)
    # description     = RichTextField(verbose_name='Text en plus', blank= True, null=True)
    description_2   = HTMLField(verbose_name='partie 1', blank= True, null=True)
    description_1   = HTMLField(verbose_name='partie 2', blank= True, null=True)
    # info_sup        = RichTextField(verbose_name='informations suplaimentaires', blank= True, null=True)
    photo           = models.ImageField(verbose_name='Photo du produit', upload_to='produits/')
    fichier_1       = models.FileField(verbose_name='Fiche technique ', upload_to='fichiers/', blank= True)
    fichier_2       = models.FileField(verbose_name='Manuel instalateur', upload_to='fichiers/', blank= True)
    fichier_3       = models.FileField(verbose_name='Manuel utilisateur', upload_to='fichiers/', blank= True)
    fichier_4       = models.FileField(verbose_name='certificat', upload_to='fichiers/', blank= True)
    is_active       = models.BooleanField(verbose_name='activer', default=True)


    def __str__(self):
        return self.designation

    class Meta:
        ordering = [F('ordre').asc(nulls_last=True)]
        verbose_name = 'Produits'
        verbose_name_plural = 'Produits'



class Slide(models.Model):
    title = models.CharField(verbose_name='titre' ,max_length= 200, blank = True)
    image = models.ImageField(upload_to= 'slides/')
    class Meta:
        verbose_name = "Photo page d'accueil"
        verbose_name_plural = "Photos page d'accueil"



DEPARTEMENT_CHOICES=[
    ('C', 'Commercial'),
    ('D', 'Direction'),
    ('M', 'Marketing'),
    ('SC', 'Service client'),
    ]

class ContactForm(models.Model):
    name        = models.CharField(max_length=50)
    departement = models.CharField(max_length=2, choices=DEPARTEMENT_CHOICES, default='D',)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20)
    subject     = models.CharField(max_length=50)
    fichier     = models.FileField(upload_to='fichiers/% d/% m/% Y/', max_length=20, blank=True)
    message     = models.TextField(blank=True)
    date_added  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formulaire de contact'



class Post(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    intro = models.CharField(max_length=200, blank=True)
    image = models.ImageField(verbose_name='Image' ,upload_to='slides/', blank= True)
    text = RichTextField(verbose_name='Article', blank= True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titre



