from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.contrib.auth.models import User

from hello.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

import requests

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return HttpResponse('<pre>' + r.text + '</pre>')

def seating(request):

    return render(request, 'seating.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

class UsersList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

