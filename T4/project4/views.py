from django.shortcuts import render
from django.db.models import Q
from app.models import blogPost

# Create your views here.
def blog_html(request):
    b = blogPost.objects.all()
    return render(request,'blog.html',{'blog':b})

def index(request):
    query = request.GET.get('q')
    if query:
        data = blogPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        data = blogPost.objects.all()
    return render(request, 'blog.html', {'data': data})