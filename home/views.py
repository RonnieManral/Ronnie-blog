from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Blog
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    blogs=Blog.objects.all()
    context = {'blogs':blogs}            
    return render(request,'blog.html',context)

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city = request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        desc=request.POST.get('desc')
        contact =Contact(name=name,email=email,phone=phone,address=address,city=city,state=state,zip=zip,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,"contact.html")

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def search(request):
    query=request.GET['query']
    blogtitle = Blog.objects.filter(title__icontains=query)
    blogcontent = Blog.objects.filter(content__icontains=query)
    blogs=blogtitle.union(blogcontent)
    params = {'blogs':blogs,'query':query}
    return render(request,'search.html',params)


    
