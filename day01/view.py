from django.http import HttpResponse
from django.shortcuts import render
# def hello(request):
#     return HttpResponse("这是我的第一个Django")
#第二版
def hello(request):
    context={}
    context['hello']="Hello,这是我的MVC版的页面"
    return render(request,'templates/hello.html',context)