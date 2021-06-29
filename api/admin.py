from django.contrib import admin

from .models import (
    Post, Hashtag
    )

# admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Hashtag)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name','owner','description',)
    # list_filter = ('name','owner','description',)
    # search_fields = ('name','owner','description',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)