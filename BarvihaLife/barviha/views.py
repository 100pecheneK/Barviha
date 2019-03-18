from django.shortcuts import render



def home(request):
    return render(request, 'barviha/index.html', {'title':'Главная страница'})

def list_1(request):
    return render(request, 'barviha/list_1.html', {'title':'Лист 1'})

def list_2(request):
    return render(request, 'barviha/list_2.html', {'title':'Лист 2'})

def list_3(request):
    return render(request, 'barviha/list_3.html', {'title':'Лист 3'})

