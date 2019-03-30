from django.shortcuts import render
from adminsite.models import Room

# Create your views here.
def mainsite(request):
	rooms = Room.objects.all()
	return render(request, 'mainsite/base.html', {'rooms': rooms})
