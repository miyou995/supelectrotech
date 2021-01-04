from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import DevisForm, ContactForm
from .models import  CATEGORY_CHOICES, Produit, Slide, Post, Tag, Post
# Create your views here.
import random


class Home(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular"] = Produit.objects.all().order_by('?')[:3]
        context["cat"] = CATEGORY_CHOICES 

        return context
    
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        return context




# class CatalogueListView(TemplateView):
#     template_name = "produits.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["cat"] = CATEGORY_CHOICES 
#         return context


class SolutionView(TemplateView):
    template_name = "solution.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        return context
    


@method_decorator(csrf_exempt, name='dispatch')
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            print('the form is valid')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            honeypot = form.cleaned_data['honeypot']

            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['inter-95@hotmail.fr']) 
            mail.send()
            messages.success(request, 'Votre message a bien été envoyer')

        return render(request, 'contact.html', {'form': form})


def error404(request, exception):
    return render(request, '404.html', status=404)


@method_decorator(csrf_exempt, name='dispatch')
class DeviFormView(FormView):
    template_name = 'base.html'
    form_class = DevisForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
    
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            # subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            # honeypot = form.cleaned_data['honeypot']
            body = 'Nom: {} \n email: {} \n Phone:{} \n Message: {}' .format(name, email, phone, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['inter-95@hotmail.fr']) 
            mail.send()
            messages.success(request, 'Votre message a bien été envoyer')
            
            # return redirect('/contact')
        return render(request, 'success.html', {'form': form})



class ProductDetailView(DetailView):
    model = Produit
    template_name = "produit-detail.html"
    context_object_name = 'produit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        return context

class ProductView(TemplateView):
    template_name = "produits.html"



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        context["intrusion"] = Produit.objects.filter(category= 'IN')
        context["intrusion"] = Produit.objects.filter(category= 'IN')
        print('balaaaaaaa',context["intrusion"].all())
        context["conventionnelle"] = Produit.objects.filter(category= 'IC')
        context["conventionnelle"] = Produit.objects.filter(category= 'IC')
        context["adressable"] = Produit.objects.filter(category= 'IA')
        context["adressable"] = Produit.objects.filter(category= 'IA')
        
        return context
    

class BlogView(ListView):
    model = Post
    context_object_name = 'posts_list'
    template_name = "blog.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        context["intrusion"] = Produit.objects.filter(category= 'IN')
        context["conventionnelle"] = Produit.objects.filter(category= 'IC')
        context["adressable"] = Produit.objects.filter(category= 'IA')
        context["categorieX"] = Produit.objects.filter(category= 'C4')
        context["categorieY"] = Produit.objects.filter(category= 'C5')
        context['tags']= Tag.objects.all()
        context['postes']= Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = CATEGORY_CHOICES 
        context["intrusion"] = Produit.objects.filter(category= 'IN')
        context["conventionnelle"] = Produit.objects.filter(category= 'IC')
        context["adressable"] = Produit.objects.filter(category= 'IA')
        context['postes']= Post.objects.all()
        return context


