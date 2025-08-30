from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    return render(request=request, template_name="base/home.html", context={"rooms": rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request=request, template_name="base/room.html", context=context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 

    context = {'form': form}
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  # pre-fill with existing data

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "base/room_form.html", {'form': form})

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, "base/delete.html", context)