from django.contrib import admin
from . import models

class Students(admin.ModelAdmin):
    """"""
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(models.Student, Students)

class Courses(admin.ModelAdmin):
    """"""
    list_display = ('id', 'course_code', 'description')
    list_display_link = ('id', 'course_code')
    search_fields = ('course_code',)

admin.site.register(models.Course, Courses)

class Enrollments(admin.ModelAdmin):
    """"""
    list_display = ('id', 'student', 'course', 'time_course')
    list_display_link = ('id',)

admin.site.register(models.Enrollment, Enrollments)
