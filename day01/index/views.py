from django.http import  HttpResponse

def index(request):
    return HttpResponse("这是我的第二个django")