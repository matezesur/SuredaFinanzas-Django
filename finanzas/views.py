from django.shortcuts import render
from pages.models import Page


def inicio(request):
    pages = Page.objects.all()[:3]
    return render(request, 'finanzas/inicio.html', {'pages': pages})


def about(request):
    return render(request, 'finanzas/about.html')
