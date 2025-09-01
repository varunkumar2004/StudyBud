from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api', #home page 
        'GET /api/rooms', # list all rooms
        'GET /api/rooms/:id', # get a single room
    ]  
    
    return Response(routes) # safe = False means we can send a list as a response eg. above

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all() # object should be converted to json before sending (serialize)
    serializer = RoomSerializer(rooms, many=True) # many=True because we are sending a list of objects
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk) # object should be converted to json before sending (serialize)
    serializer = RoomSerializer(room, many=False) # many=True because we are sending a list of objects
    return Response(serializer.data)