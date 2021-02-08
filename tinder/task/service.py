import socket
from django.core.exceptions import ObjectDoesNotExist


def filter_group(request):
    from .models import User

    if User.objects.get(name=request.user).group == 'base':
        return User.objects.all()[:11]
    elif User.objects.get(name=request.user).group == 'premium':
        return User.objects.all()[:101]
    elif User.objects.get(name=request.user).group == 'vip':
        return User.objects.all()
    else:
        print('no')

# def comment(request):
#     from .models import User
#     comment_text = User.objects.get(comment=request.comment)