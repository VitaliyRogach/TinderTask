from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.gis.db import models as gis_models

from task import service


class Profile(models.Model):
    rate = (
        ('Base', 'base'),
        ('Premium', 'premium'),
        ('VIP', 'vip'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255)
    description = models.TextField("Description", max_length=255)
    pictures = models.ImageField(upload_to='media/')
    age = models.IntegerField(null=False, blank=True)
    group = models.CharField(max_length=255, choices=rate, default='base', null=True)
    geo_location = gis_models.PointField(srid=4326, null=True, blank=True, default=service.get_location())
    def __str__(self):
        return self.name


class Content(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    image = models.ImageField(upload_to='media/')
    description = models.CharField("Description", max_length=3000)

    def __str__(self):
        return self.description


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

class Like(models.Model):
    like = models.BooleanField(default=False)
    userliker = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
