from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from beauty_center import settings


class Service(models.Model):
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Stylist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    description = models.TextField()
    # services = models.ManyToManyField(Service)
    active = models.BooleanField(default=True)
    profile = models.ImageField(null=True, blank=True, upload_to="stylist_profile/")

    def stars_avg(self):
        return Review.objects.filter(stylist=self).aggregate(Avg('stars'))['stars__avg']

    def stars_count(self):
        return Review.objects.filter(stylist=self).count()

    def __str__(self):
        return self.name


class StylistService(models.Model):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.service} Expert: {self.stylist}'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stylist_service = models.ForeignKey(StylistService, on_delete=models.CASCADE)
    # stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    # services = models.ForeignKey(StylistService, on_delete=models.CASCADE)
    status = models.CharField(max_length=32,
                              choices=[('Pending', 'Pending'), ("Confirmed", "Confirmed"), ("Declined", "Declined")])
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField(null=True, blank=True)


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


class AboutUs(models.Model):
    description = models.TextField()


class Contact(models.Model):
    description = models.TextField()


# @receiver(post_save, sender="")
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         send_mail("object", "content", settings.EMAIL_HOST_USER,[])
