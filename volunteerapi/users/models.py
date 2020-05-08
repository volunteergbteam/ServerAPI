from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(verbose_name="First Names", blank=False, max_length=64)
    second_name = models.CharField(verbose_name="Second Names", blank=False, max_length=64)