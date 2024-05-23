from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models


class Stylist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=32,
                              choices=[('Pending', 'Pending'), ("Confirmed", "Confirmed"), ("Declined", "Declined")])
    datetime = models.DateTimeField()


class Schedule(models.Model):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    time_from = models.TimeField()
    time_to = models.TimeField()
    date = models.DateField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    description = models.TextField()
