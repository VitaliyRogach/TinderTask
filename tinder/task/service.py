import socket
from django.core.exceptions import ObjectDoesNotExist


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def filter_group(request):
    from .models import UserInf

    if UserInf.objects.get(name=request.user).group == 'base':
        return UserInf.objects.all()[:11]
    elif UserInf.objects.get(name=request.user).group == 'premium':
        return UserInf.objects.all()[:101]
    elif UserInf.objects.get(name=request.user).group == 'vip':
        return UserInf.objects.all()
    else:
        print('no')
