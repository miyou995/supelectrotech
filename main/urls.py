
from django.contrib import admin
from django.urls import path
from .views import Home, AboutView, ContactView,  ProductView, ProductDetailView
urlpatterns = [
    path('', Home.as_view(), name= 'index'),
    path('about/', AboutView.as_view(), name= 'about'),
    path('produits/', ProductView.as_view(), name= 'produits'),
    path('contact/', ContactView.as_view(), name= 'contact'),
    path('produits/<slug:slug>/', ProductDetailView.as_view(), name= 'produit-detail'),
]

