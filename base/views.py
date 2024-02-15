from django.shortcuts import render
from .models import Room

# Create your views here.
# rooms_data = [
#     {
#         'id': 1,
#         'name': 'Let\'s learn python',
#         'instructor': 'John Doe',
#     },
#      {
#         'id': 2,
#         'name': 'Vue is an amazing framework',  
#         'instructor': 'John Doe',
#     },
#      {
#         'id': 3,
#         'name': 'Design with me',
#         'instructor': 'Jason Derulo',
#     },

   
# ]

def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms':rooms
    }   
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room
    }
    return render(request, 'base/room.html', context)