from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    rate = (
        ('Base', 'base'),
        ('Premium', 'premium'),
        ('VIP', 'vip'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField("Description", max_length=255)
    pictures = models.ImageField("Pictures", upload_to='post/')
    age = models.IntegerField(max('101'), min('18'))
    group = models.CharField(max_length=255, choices=rate, default='base', null=True)

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
        User.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            User.objects.create(user=instance)