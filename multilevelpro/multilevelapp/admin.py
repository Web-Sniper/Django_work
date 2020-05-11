from django.contrib import admin
from .models import Emp,Student,Cust

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']
class AdminCust(admin.ModelAdmin):
    list_display = ['cname','sales']

admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)
admin.site.register(Cust,AdminCust)