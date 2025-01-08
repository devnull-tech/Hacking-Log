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
    logs = models.Log.objects.filter(platform=platform, is_public=True)
    return render(request, 'hacklog/index.html', {
        'layout_data': layout_data,
        'logs': logs
    })

def log(request, log_id):
    layout_data = Layout.objects.filter(in_use=True).first()
    log = get_object_or_404(models.Log, id=log_id, is_public=True)
    return render(request, 'hacklog/log.html', {
        'layout_data': layout_data,
        'log': log
    })

def glosary(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_terms = models.Term.objects.all()
    return render(request, 'hacklog/terms.html', {
        'layout_data': layout_data,
        'terms': all_terms
    })

def term(request, term_id):
    layout_data = Layout.objects.filter(in_use=True).first()
    term = get_object_or_404(models.Term, id=term_id)
    term_as_list = []
    term_as_list.append(term)
    return render(request, 'hacklog/terms.html', {
        'layout_data': layout_data,
        'terms': term_as_list
    })
    
def tips(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_tips = models.Tip.objects.all()
    return render(request, 'hacklog/tips.html', {
        'layout_data': layout_data,
        'tips': all_tips
    })
