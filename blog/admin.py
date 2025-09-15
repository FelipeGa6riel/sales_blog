from django.contrib import admin
from django.http import HttpRequest
from django.urls import URLPattern, URLResolver, path
from django.utils.html import format_html

from blog.models import Post, Profile, Tag, Category
from blog.views import ProfileAdminLogin

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "tags_count",
        "is_published",
        "created_at",
        "is_deleted",
    )

    def tags_count(self, objt):
        if objt.tags.exists():
            count = objt.tags.count()
            return format_html('<span class="badge badge-info">{}</span>', count)
        return 0

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(author__user=request.user)

        return qs


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)

        return qs


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "is_published", "created_at", "is_deleted")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "is_published", "created_at")


class ProfileAdminSite(admin.AdminSite):
    site_header = "Profile Admin"
    site_title = "Profile"
    index_title = "Welcome"

    def get_urls(self) -> list[URLResolver | URLPattern]:
        urls = super().get_urls()

        profile_login = [
            path("login/", ProfileAdminLogin.as_view(), name="login_profile")
        ]

        return profile_login + urls

    def has_permission(self, request: HttpRequest) -> bool:
        return request.user.is_active and request.user.has_perm(
            "blog.can_access_profile_admin"
        )


profile_admin_site = ProfileAdminSite(name="profile_admin")

profile_admin_site.register(Profile, ProfileAdmin)
profile_admin_site.register(Post, PostAdmin)
profile_admin_site.register(Tag, TagAdmin)
profile_admin_site.register(Category, CategoryAdmin)
