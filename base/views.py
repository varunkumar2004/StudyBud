from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm

# dont name it login as it will conflict with django login function
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, 'User does not exist.')
            
        user = authenticate(request, username=username, password=password)
        
        if (user is not None):
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'Username or password does not exist.')
        
    context = {}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # Q -> used for complex queries with and or conditions
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) | 
        Q(description__icontains=q) 
    )

    topics = Topic.objects.all() 

    context= {
        "rooms": rooms, 
        "topics": topics,
        "room_count": rooms.count()
    }

    return render(request=request, template_name="base/home.html", context=context)

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