from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # url('admin/', admin.site.urls),
    # url(r'about/$', views.about),
    url(r'^$', views.article_list),
]

# urlpatterns += staticfiles_urlpatterns()
