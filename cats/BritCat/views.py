from django.shortcuts import render

def BritCat(request):
    return render(request, 'site_cats/index.html')