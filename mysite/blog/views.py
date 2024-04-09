from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post



def post_list(request):
    posts = Post.Published.all()
    # return render(request,     
    #               "blog/post/list.html",
    #               {"posts":posts})

    return render(request,
                  "blog/posts/list.html",
                  {"posts":posts})

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                              status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request,
                  "blog/posts/detail.html",
                  {"post":post})

