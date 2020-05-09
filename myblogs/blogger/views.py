from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import BlogContent

def index(request):
    latest_blog_list = BlogContent.objects.order_by('post_date')[:5]
    template = loader.get_template('blogger/index.html')
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, blog_id):
    return HttpResponse("You're looking at question %s." % blog_id)

def Contact(request):    
    return render(request, 'blogger/Contact.html')

def BlogPage(request):    
    return render(request, 'blogger/BlogPage.html')