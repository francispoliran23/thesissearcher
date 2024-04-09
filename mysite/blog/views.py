from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.paginator import Paginator
from .models import Post



def post_list(request):
    post_list = Post.Published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    return render(request,
                  "blog/posts/list.html",
                  {"posts":posts})

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                              status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request,
                  "blog/posts/detail.html",
                  {"post":post})

