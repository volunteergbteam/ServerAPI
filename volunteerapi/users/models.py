from django.db import models

# Create your models here.


class User(models.Model):

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    first_name = models.CharField(verbose_name="First Names", blank=False, max_length=64)
    second_name = models.CharField(verbose_name="Second Names", blank=False, max_length=64)