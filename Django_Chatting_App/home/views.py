from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return render(request,"home.html",{})


def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room_name = request.POST["room_name"]
    username = request.POST["username"]
    if Room.objects.filter(name = room_name).exists():
        return redirect("/"+room_name+"?username="+username)
    else:
        Room.objects.create(name = room_name)
        return redirect("/"+room_name+"?username="+username)

def send(request):
    message = request.POST["message1"]
    room_id = request.POST["room_id"]
    username = request.POST["username"]
    new_message = Message.objects.create(value = message,user= username,room = room_id)
    new_message.save()
    return HttpResponse("message has been send")

def getMessages(request,room):
    room_details = Room.objects.get(name = room)
    messge_info = Message.objects.filter(room = room_details.id)
    return JsonResponse({"messages":list(messge_info.values())})