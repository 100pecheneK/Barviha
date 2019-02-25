from django.shortcuts import render

news = [
    {
        'title': 'Первая Запись',
        'text': 'Просто большой текс для первой записи',
        'data': '22 февраля'
    }
]

def home(request):
    data = {
        'home' : home,
        'title': 'Главная страница'
    }
    return render(request, 'barviha/index.html', data)

def list_1(request):
    return render(request, 'barviha/list_1.html', {'title':'Лист 1'})

