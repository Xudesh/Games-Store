from django.contrib import admin
from .models import Post,Comment,Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
