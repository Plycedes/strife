from django.shortcuts import render

rooms =[
    {'id':1, 'name':'Unity Scripting'},
    {'id':2, 'name':'Angular Delvelopers'},
    {'id':3, 'name':'Blender tips'},
]

def home(request):    
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i    
    return render(request, 'base/room.html', {'room': room})
