from django.shortcuts import render
#第二版
def hello(request):
    context={}
    context['hello']="Hello,这是我的MVC版的页面"
    return render(request,'templates/hello.html',context)