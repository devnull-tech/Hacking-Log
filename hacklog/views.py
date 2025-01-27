from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import Layout
from . import models

def home_redirect(request):
    return redirect('home')

def index(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    logs = models.Log.objects.filter(is_public=True)
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

@login_required
def glosary(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_terms = models.Term.objects.all()
    return render(request, 'hacklog/terms.html', {
        'layout_data': layout_data,
        'terms': all_terms
    })

@login_required
def term(request, term_id):
    layout_data = Layout.objects.filter(in_use=True).first()
    term = get_object_or_404(models.Term, id=term_id)
    term_as_list = []
    term_as_list.append(term)
    return render(request, 'hacklog/terms.html', {
        'layout_data': layout_data,
        'terms': term_as_list
    })

@login_required    
def tips(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_tips = models.Tip.objects.all()
    return render(request, 'hacklog/tips.html', {
        'layout_data': layout_data,
        'tips': all_tips
    })
