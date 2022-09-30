from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    a = request.GET.get('a')
    print(a)
    b = request.GET.get('b')
    print(b)
    r = HttpResponse(f'{int(a)+int(b)}')
    return r

urlpatterns = [
    path('', home),
]
