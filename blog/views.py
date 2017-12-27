from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import BlogPost
from .forms import BlogPostForm


def post_list(request):
    blog_posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'blog_posts': blog_posts})


def post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'blog_post': blog_post})


def post_new(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.published_date = timezone.now()
            blog_post.save()
            return redirect('post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.published_date = timezone.now()
            blog_post.save()
            return redirect('post_detail', pk=pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/post_edit.html', {'form': form})
