from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(requst):
    if requst.method == 'POST':
        user_name = requst.POST.get('username', '')
        pass_word = requst.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(requst, user)
            return render(requst, 'index.html')
        else:
            return render(requst, 'login.html', {'msg': '用户名和密码错误'})
    elif requst.method == 'GET':
        return render(requst, 'login.html')