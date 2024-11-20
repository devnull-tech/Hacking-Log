from django.shortcuts import render
from . import models

def home(request):
    layout_data = models.Layout.objects.filter(in_use=True).first()
    return render(request, 'home.html', {
        'layout_data': layout_data
    })

def contact(request):
    layout_data = models.Layout.objects.filter(in_use=True).first()
    return render(request, 'contact.html', {
        'layout_data': layout_data
    })
