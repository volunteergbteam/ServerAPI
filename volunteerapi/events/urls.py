from django.contrib import admin
from django.urls import path, include
from .views import EventCreateView

urlpatterns = [
    path('event/create/', EventCreateView.as_view())
]