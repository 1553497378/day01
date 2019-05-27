from django.http import  HttpResponse

def hello(request):
    return HttpResponse("这是我的第一个django")