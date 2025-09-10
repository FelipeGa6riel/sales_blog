from typing import Any

from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseBase
from django.shortcuts import render

from blog.models import Post

# Create your views here.

"""Manager for admin profile login, requested only is_active and custom permission"""


class ProfileAdminLogin(LoginView):
    template_name = "admin/login.html"

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        if request.user.is_authenticated:
            if request.user.has_perm("can_access_profile_admin"):
                return super(LoginView, self).dispatch(request, *args, **kwargs)
            else:
                return HttpResponse("<p>Forbiden</p>")

        return super().dispatch(request, *args, **kwargs)


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
