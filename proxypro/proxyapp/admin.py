from django.contrib import admin
from .models import Emp,EmpProxy

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','location','salary']
class AdminProxyEmp(admin.ModelAdmin):
    list_display = ['ename', 'location', 'salary']

admin.site.register(Emp,AdminEmp)
admin.site.register(EmpProxy,AdminProxyEmp)
