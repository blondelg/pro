from django.contrib import admin
from django.urls import path, include, re_path
from home.urls import urlpatterns as home_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pro_app.urls')),

] + home_urlpatterns
