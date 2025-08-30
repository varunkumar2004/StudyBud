from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request=request, template_name="base/home.html", context={"rooms": rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request=request, template_name="base/room.html", context=context)