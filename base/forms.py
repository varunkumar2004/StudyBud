from django.forms import ModelForm
from .models import Room,  User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #create inputs for all the fields in room 
        exclude = ['host', 'participants'] # exclude host and participants fields from the form
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar', 'bio'] 
        