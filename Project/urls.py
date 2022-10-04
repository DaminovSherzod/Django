from django.urls import path
from myapp.views import home, about, index, contact
    
urlpatterns = [
    path('', home),
    path('about/', about),
    path('index/', index),
    path('contact/', contact)
]
