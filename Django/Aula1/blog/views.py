from django.shortcuts import render
from typing import Any
from . import date
from django.http import HttpRequest, Http404
# Create your views here.

def blog(request):
    print('blog')
    content = {
            #'text': 'Welcome blog',
            'posts': date.posts
    }

    return render(
        request,
        'blog/index.html',
        content
    )

def post(request: HttpRequest, post_id:int):
    found_post: dict[str, Any] | None = None

    for post in date.posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não exesite')

    content = {
            #'text': 'Welcome blog',
            'post': found_post,
            'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        content
    )


def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        {
            'text': 'Welcome Exemplo'
        }
    )
