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

def post_details(request, id):
    post = get_object_or_404(Post,
                              id=id,
                              status=Post.Status.PUBLISHED)
    return render(request,
                  "blog/posts/detail.html",
                  {"post":post})