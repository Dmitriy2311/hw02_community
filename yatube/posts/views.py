from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_LIMIT = 10


# Create your views here.
def index(request):
    post1 = Post.objects.all()[:POST_LIMIT]
    return render(request, 'posts/index.html', {"posts": post1})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:POST_LIMIT]
    return render(request, 'posts/group_list.html',
                  {"group": group, "posts": posts}
                  )
