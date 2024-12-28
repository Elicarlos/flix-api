from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer