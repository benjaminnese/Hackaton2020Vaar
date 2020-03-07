from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import Group

admin.site.unregister(Group)
admin.site.index_title = "Her kan du legge til ny arragement"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

