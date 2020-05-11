from django.db import models
# from users.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Cities(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(verbose_name="names", max_length=64, blank=False)


class EventType(models.Model):

    def __str__(self):
        return self.type

    type = models.CharField(verbose_name='Event Types', max_length=64)
    description = models.CharField(verbose_name='Descriptions', max_length=128)
    avatar = models.ImageField(upload_to='uploads/', max_length=128)
    rating = models.IntegerField()


class Event(models.Model):

    title = models.CharField(verbose_name='Titles', max_length=128)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    type_id = models.ForeignKey(EventType, verbose_name='Event Types', on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Descriptions', max_length=256)
    event_date = models.DateTimeField(verbose_name="Events Dates", auto_now=False, auto_now_add=False)
    is_over = models.BooleanField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    in_progress = models.BooleanField()
    location_lon = models.FloatField()
    location_lat = models.FloatField()
    location_id = models.ForeignKey(Cities, on_delete=models.CASCADE)
