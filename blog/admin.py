from django.contrib import admin

from blog.models import Post, Profile, Tag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at", "is_deleted")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "is_published", "created_at", "is_deleted")
