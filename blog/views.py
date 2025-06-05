from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(req):
    posts = Post.objects.order_by('-published_at')
    return render(req, 'blog/post_list.html', {'posts' : posts})