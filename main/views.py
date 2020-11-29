from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import ContactForm, CATEGORY_CHOICES, Produit, Slide, Post
# Create your views here.

class Home(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["slides"] = Slide.objects.all()
        # context["cat_prod"] = Categorie_produit.objects.all()
        # context["cat_sol"] = Categories_Solution.objects.all()
        return context
    
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["slides"] = SliderAPropos.objects.all()
        # context["cat_prod"] = Categorie_produit.objects.all()
        # context["cat_sol"] = Categories_Solution.objects.all()

        return context




class CatalogueListView(TemplateView):
    template_name = "produits.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SolutionView(TemplateView):
    template_name = "solution.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["cat_sol"] = Categories_Solution.objects.all()
        return context
    



class ContactView(TemplateView):
    template_name = "contact.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["cat_sol"] = Categories_Solution.objects.all()
        return context
    

class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # form = self.get_form()
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Votre message a bien été envoyer')
        else:
            print(form.errors)
            messages.error(request, 'Vérifier vos données et réessayer')
        return redirect('/contact')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["cat_sol"] = Categories_Solution.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Produit
    template_name = "produit-detail.html"
    context_object_name = 'produit'



class ProductView(TemplateView):
    template_name = "produits.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        context["intrusion"] = Produit.objects.filter(category= 'IN')
        context["conventionnelle"] = Produit.objects.filter(category= 'IC')
        context["adressable"] = Produit.objects.filter(category= 'IA')
        
        return context
    
