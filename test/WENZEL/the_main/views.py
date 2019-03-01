from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

def test(request):

    form_post = PostForm(request.POST)
    return render(request, 'the_main/test.html', {'form': form_post, 'title': 'test страница'}, locals)

def home(request):

    form = SubscribersForm(request.POST or None)
    if request.method =="POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        username = form.cleaned_data.get('username')
        messages.success(request, f'Пользователь {username} был успешно зарегистрирован!')
        new_form =form.save()
        return redirect('the_main-site')
    
    return render(request, 'the_main/home.html', {'form': form, 'title': 'Главная страница'})

def contacti(request):
    return render(request, 'the_main/contacti.html', {'title': 'Страничка контакты'})

def site(request):
    return render(request, 'the_main/site.html', {'title': 'сайт'})