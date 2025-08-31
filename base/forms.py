from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #create inputs for all the fields in room 
        exclude = ['host', 'participants'] # exclude host and participants fields from the form
        