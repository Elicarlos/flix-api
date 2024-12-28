from django.shortcuts import render
from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    
class ActorRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
