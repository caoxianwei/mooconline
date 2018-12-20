# Author:Sunday
from django.urls import path,include,re_path

from .views import UserinfoView

app_name = 'users'

urlpatterns = [
    #用户信息
    path("info/", UserinfoView.as_view(),name='user_info'),
]