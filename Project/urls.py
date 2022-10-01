from django.urls import path
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    a = request.GET.get('a',0)
    print(a)
    b = request.GET.get('b',0)
    print(b)
    r = HttpResponse(int(a)+int(b))
    return r
    # if a!=None and b!=None:
    #     r = HttpResponse(int(a)+int(b))
    #     return r
    # elif a==None and b==None:
    #     r = HttpResponse('0')
    #     return r
    # elif a==None:
    #     r = HttpResponse(b)
    #     return r
    # elif b==None:
    #     r = HttpResponse(a)
    #     return r

urlpatterns = [
    path('', home),
]
