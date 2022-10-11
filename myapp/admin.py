from django.contrib import admin
from .models import Friend, Person
# Register your models here.

admin.site.register(Person)
admin.site.register(Friend)