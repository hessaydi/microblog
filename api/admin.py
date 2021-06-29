from django.contrib import admin

from .models import (
    Post, Hashtag
    )

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_deleted',)
    list_filter = ('title', 'owner', 'is_deleted',)
    search_fields = ('title', 'owner', 'is_deleted',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)