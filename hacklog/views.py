from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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
    if request.method == 'GET':
        return render(request, 'hacklog/log.html', {
            'layout_data': layout_data,
            'log': log
        })
    if request.method == 'POST':
        question = request.POST.get('question')
        bot = get_list_or_404(models.Bot, in_use=True)[0]
        answer = bot.send_prompt(question)
        return render(request, 'hacklog/log.html', {
            'layout_data': layout_data,
            'log': log,
            'question':question,
            'answer': answer['text']
        })

def glosary(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_terms = models.Term.objects.all()
    return render(request, 'hacklog/terms.html', {
        'layout_data': layout_data,
        'terms': all_terms
    })
    
def tips(request):
    layout_data = Layout.objects.filter(in_use=True).first()
    all_tips = models.Tip.objects.all()
    return render(request, 'hacklog/tips.html', {
        'layout_data': layout_data,
        'tips': all_tips
    })
