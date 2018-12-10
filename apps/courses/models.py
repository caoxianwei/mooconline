from datetime import datetime

from django.db import models

# Create your models here.

'''课程'''


class Course(models.Model):
    degree_choices = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级'),
    )
    name = models.CharField('课程名称', max_length=50)
    desc = models.CharField('课程描述', max_length=300)
    detail = models.TextField('课程详情')
    degree = models.CharField(choices=degree_choices, max_length=100)
    learn_times = models.IntegerField('学习时长(分钟数)', default=0)
    students = models.IntegerField('学习人数', default=0)
    image = models.ImageField(upload_to='courses/%Y/%m', max_length=100)
    click_nums = models.IntegerField("点击数", default=0)
    tag = models.CharField('课程标签', default='', max_length=10)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField('章节名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name


# '''章节视频'''
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField('视频名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField('视频名', max_length=100)
    download = models.FileField('资源文件', upload_to='course/resource/%Y/%m', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
