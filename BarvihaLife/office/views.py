from django.shortcuts import render



def main(request):
    return render(request, 'office/main.html', {'title':'Главная страница'})

def list_1(request):
    return render(request, 'office/list_1.html', {'title':'Лист 1'})



