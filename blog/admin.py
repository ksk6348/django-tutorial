from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text")
    fields = ("title", "text")


admin.site.register(Post)
