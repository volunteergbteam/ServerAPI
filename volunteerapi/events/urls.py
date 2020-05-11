from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('event/create/', EventCreateView.as_view()),
    path('event/read/', EventListView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view()),
    path('city/create/', CityCreateView.as_view()),
]
