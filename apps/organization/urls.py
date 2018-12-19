# Author:Sunday

from django.urls import path, re_path

from .views import OrgView, AddUserAskView

app_name = "organization"

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
]
