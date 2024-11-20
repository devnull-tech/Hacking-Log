from django.shortcuts import render, redirect, get_object_or_404
from home.models import Layout
from . import models

def home_redirect(request):
    return redirect('home')

def index(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    platform = None
    if request.path == "/hacklog/vulnhub/":
        platform = "VH"
    if request.path == "/hacklog/hackthebox/":
        platform = "HTB"
    logs = models.Log.objects.filter(platform=platform)
    return render(request, 'hacklog/index.html', {
        'layout_data': layout_data,
        'logs': logs
    })

def log(request, log_id):
    layout_data = Layout.objects.filter(in_use=True).first()
    log = get_object_or_404(models.Log, id=log_id)
    return render(request, 'hacklog/log.html', {
        'layout_data': layout_data,
        'log': log
    })
