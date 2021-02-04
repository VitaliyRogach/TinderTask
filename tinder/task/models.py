from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class UserInf(models.Model):
    rate = (
        ('Base', 'base'),
        ('Premium', 'premium'),
        ('VIP', 'vip'),
    )

    name = models.CharField("Name", max_length=255, unique=True)
    discription = models.TextField("Discription", max_length=3000)
    pictures = models.ImageField("Pictures", upload_to='post/')
    age = models.IntegerField(max('101'), min('18'))
    group = models.CharField(max_length=255, choices=rate, default='base', null=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль')
    image = models.ImageField(upload_to='media/')
    description = models.CharField("Discription", max_length=3000)

    def __str__(self):
        return self.description

# @receiver(post_save, sender=User)
# def save_or_create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserInf.objects.create(user=instance)
#     else:
#         try:
#             instance.profile.save()
#         except ObjectDoesNotExist:
#             UserInf.objects.create(user=instance)