from djangoproject2 import views
from django.urls import path

from django.contrib import admin
urlpatterns = [
    path("", views.home),
    path("ccu408310044", views.ccu408310044_function),
    path("admin/", admin.site.urls)
]
