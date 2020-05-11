from django.contrib import admin
from .models import Emp,Student,Cust

class AdminEmp(admin.ModelAdmin):
    list_display = ['name','location','salary']
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','fee']
class AdminCust(admin.ModelAdmin):
    list_display = ['name','location','sales']

admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)
admin.site.register(Cust,AdminCust)
