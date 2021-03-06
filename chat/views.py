from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room):
    return render(request, 'chat/room.html', {
        'room_json': mark_safe(json.dumps(room))
    })
