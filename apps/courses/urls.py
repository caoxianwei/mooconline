# Author:Sunday

from django.urls import path

from .views import CourseListView

app_name = 'course'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list')
]