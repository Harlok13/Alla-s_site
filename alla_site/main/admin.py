from django.contrib import admin

from main.models import Posts, Category


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
