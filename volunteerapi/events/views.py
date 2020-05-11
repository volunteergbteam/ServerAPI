from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Event
from .permissions import IsOwnerOrReadOnly


class EventCreateView(generics.CreateAPIView):
    """
    Создаёт событие пользователя
    """
    serializer_class = EventDetailSerializer


class EventListView(generics.ListAPIView):
    """
    Выводит список событий пользователя
    """
    serializer_class = EventListSerializer
    queryset = Event.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    В зависимости от типа запроса будет либо выводить данные,
    либо удалять их, либо апдейтить.
    """
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    #permission_classes = IsOwnerOrReadOnly()


class CityCreateView(generics.CreateAPIView):
    serializer_class = CityDetailSerializer

