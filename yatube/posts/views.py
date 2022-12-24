from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_LIMIT = 10


# Create your views here.
def index(request):
    post = Post.objects.all()[:POST_LIMIT]
    return render(request, 'posts/index.html', {"posts": post})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_LIMIT]
    return render(
        request,
        'posts/group_list.html',
        {"group": group, "posts": posts}
    )
