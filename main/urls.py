from . import views
from django.contrib import admin
from django.urls import path
from .views import Home, AboutView, ContactView,  ProductView, ProductDetailView, BlogView, PostDetailView, DeviFormView
urlpatterns = [
    path('', Home.as_view(), name= 'index'),
    path('about/', AboutView.as_view(), name= 'about'),
    path('articles/', BlogView.as_view(), name= 'blog'),
    path('produits/', ProductView.as_view(), name= 'produits'),
    path('contact/', ContactView.as_view(), name= 'contact'),
    path('detail/', PostDetailView.as_view(), name= 'detaail'),
    path('devis-form/', DeviFormView.as_view(), name= 'devis-form'),
    path('produits/<slug:slug>/', ProductDetailView.as_view(), name= 'produit-detail'),
    path('articles/<slug:slug>/', PostDetailView.as_view(), name= 'post-detail'),
]

