from django.contrib import admin

from main.models import Posts, Category


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'time_create', 'time_update', 'photo', 'is_published')
    list_display_links = ('title', 'id')
    list_editable = ('is_published',)
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'time_update', 'is_published')



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
