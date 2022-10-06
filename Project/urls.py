from django.urls import path
from myapp.views import home, about, index, contact
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls)
]
