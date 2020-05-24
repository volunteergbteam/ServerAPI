from rest_framework import serializers
from .models import Event, Cities


class EventDetailSerializer(serializers.ModelSerializer):

    # owner_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'creation_date', 'type_id', 'description', 'event_date')


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
