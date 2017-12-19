from django.shortcuts import render
from django.utils import timezone

from .models import BlogPost


def post_list(request):
    blog_posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'blog_posts':  blog_posts})
