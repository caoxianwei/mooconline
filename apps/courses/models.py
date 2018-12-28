from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher

# Create your models here.

'''课程'''


class Course(models.Model):
    degree_choices = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级'),
    )
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构", null=True, blank=True)
    name = models.CharField('课程名称', max_length=50)
    desc = models.CharField('课程描述', max_length=300)
    detail = models.TextField('课程详情')
    is_banner = models.BooleanField('是否轮播',default=False)
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',null=True,blank=True,on_delete=models.CASCADE)
    degree = models.CharField(choices=degree_choices, max_length=100)
    learn_times = models.IntegerField('学习时长(分钟数)', default=0)
    students = models.IntegerField('学习人数', default=0)
    image = models.ImageField(upload_to='courses/%Y/%m', max_length=100)
    click_nums = models.IntegerField("点击数", default=0)
    category = models.CharField("课程类别", max_length=20, default=''),
    tag = models.CharField('课程标签', default='', max_length=10),
    youneed_know = models.CharField('课程须知', max_length=300, default='')
    teacher_tell = models.CharField('老师告诉你', max_length=300, default='')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程的章节数
        return self.lesson_set.all().count()


    def get_course_lesson(self):
        #获取课程所有章节
        return self.lesson_set.all()

    def get_learn_users(self):
        #获取这门课程的学习用户
        return self.usercourse_set.all()[:5]

    get_zj_nums.short_description = '章节数'  # 在后台显示的名称

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = u'轮播课程'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField('章节名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


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
