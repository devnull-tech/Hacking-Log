from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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

def register(request):
    layout_data = models.Layout.objects.filter(in_use=True).first()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form': form,
        'layout_data': layout_data
        })

def login_view(request):
    layout_data = models.Layout.objects.filter(in_use=True).first()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('home')
    return render(request, 'login.html', {
        'layout_data': layout_data
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
