from django.contrib import admin
from blog.models import Post, Tag, Category
# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    ordering = ('-created_time', )
    list_filter = ['created_time']


admin.site.register(Post, postAdmin)
admin.site.register(Tag)
admin.site.register(Category)