from django.contrib import admin
from .models import Student,Course

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','email','location']
class AdminCourse(admin.ModelAdmin):
    list_display = ['cname','cfee']
admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)
