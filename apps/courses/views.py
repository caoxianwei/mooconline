from django.shortcuts import render
from django.views.generic import View

from .models import Course, CourseResource, Video

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class CourseListView(View):
    '''课程列表'''

    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        # 热门课程推荐
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 2, request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            'all_courses': courses,
            'hot_courses': hot_courses,
        })
