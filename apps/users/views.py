from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def user_login(requst):
    if requst.method == 'POST':
        user_name = requst.POST.get('username', '')
        pass_word = requst.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(requst, user)
            return render(requst, 'index.html')
        else:
            return render(requst, 'login.html')
    elif requst.method == 'GET':
        return render(requst, 'login.html')