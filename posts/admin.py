from django.contrib import admin
from posts.models import Post,PostImage,Comment
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
import admin_thumbnails

class CommentInline(admin.TabularInline): #ForeignKey로 연결된 다른 객체 보기
    model = Comment
    extra = 1
    
@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline): #ForeignKey로 연결된 다른 객체 보기
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        "id","content",
    ]
    inlines=[
        CommentInline,
        PostImageInline,
    ]
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display=[
        "id","post","photo"
    ]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=[
        "id","post","content",
    ]
    

    