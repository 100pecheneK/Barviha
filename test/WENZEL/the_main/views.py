from django.shortcuts import render
from django.http import HttpResponse

news = [
    { 
        'title': 'Мой первая запись',
        'text': 'Широко живут здесь люди',
        'date': '18 января 2019',
        'avtor': ' wenzel.w'

    },
    {
        'title': 'Вторая запись',
        'text': 'Ты опять стоишь у порога',
        'date': '18 февраля 2019',
        'avtor': ''

    }
]

def home(request):
    data = {
        'news': news,
        'title': 'Главная страница'
    }
    return render(request, 'the_main/home.html', data)

def contacti(request):
    return render(request, 'the_main/contacti.html', {'title': 'Страничка контакты'})

def site(request):
    return render(request, 'the_main/site.html', {'title': 'сайт'})