from django.conf.urls import include, url
from django.contrib import admin
from courses import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'firstpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^contact/', views.contact),
    url(r'^feedback/',views.feedback),
    url(r'^date/', views.date),
    url(r'^$', views.home)
]
