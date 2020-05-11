from django.contrib import admin
from .models import Emp,Cust,Student

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']
class AdminCust(admin.ModelAdmin):
    list_display = ['cname','sales']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']

admin.site.register(Emp,AdminEmp)
admin.site.register(Cust,AdminCust)
admin.site.register(Student,AdminStudent)
