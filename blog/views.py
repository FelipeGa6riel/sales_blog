from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index_posts(request):
    if request.GET.get("tag"):
        url_qr = request.GET.get("tag")
        posts = Post.objects.filter(tags__name=url_qr)

        return render(request, "index.html", {"posts": posts})

    posts = Post.objects.all()

    return render(request, "index.html", {"posts": posts})


def post_detail(request, pk, title):
    post = Post.objects.get(pk=pk)

    return render(request, "post_detail.html", {"post": post})


def post_by_tag(request):
    url_qr = request.GET.get("tag")
    posts = Post.objects.get_queryset().filter(url_qr)
    return render(request, "index.html", {"posts": posts})
