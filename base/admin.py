from django.contrib import admin
from .models import Room, Topic, Message, User

# dont have to register User model as it is already registered in django admin
# Register others models here
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)