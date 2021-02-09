import socket
from django.core.exceptions import ObjectDoesNotExist


def filter_group(request):
    """Функция фильтрации пользователей на 3 уровня доступа(Base, Premium, Vip)"""
    from .models import User

    if User.objects.get(name=request.user).group == 'base':
        return User.objects.all()[:11]
    elif User.objects.get(name=request.user).group == 'premium':
        return User.objects.all()[:101]
    elif User.objects.get(name=request.user).group == 'vip':
        return User.objects.all()
    else:
        print('no')

