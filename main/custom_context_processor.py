from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DevisForm


def devisFormView(request):
    return {'devis_form': DevisForm()}