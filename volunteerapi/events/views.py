from django.shortcuts import render
from rest_framework import generics
from .serializers import EventDetailSerializer


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer

