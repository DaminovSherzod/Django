from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    a = request.POST
    print(type(a))
    # b = request.POST.get('b',0)
    # print(b)
    r = JsonResponse({'sum':int(a.get('a'))+int(a.get('b'))})
    return r

def about(request):
    
    return HttpResponse("<h1>About</h1>")

def index(request):
    
    return HttpResponse("<h1>Index</h1>")

def contact(request):
   
    return HttpResponse("<h1>Contact</h1>")