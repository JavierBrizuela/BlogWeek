from django.contrib import admin
from .models import Category, Tag, Post, About, Link

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Tag, TagAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'published', 'author', 'created', 'post_tag')
    readonly_fields = ('created', 'updated')
    list_filter = ('category', 'tag', 'author__username')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    ordering = ['author', '-created']

    def post_tag(self, obj):
        return ' - '.join([t.name for t in obj.tag.all().order_by('name')])
    post_tag.short_description = 'Etiquetas'

admin.site.register(Post, PostAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description', 'created')

admin.site.register(About, AboutAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name','key', 'url')
    readonly_fields = ('created', 'updated')

admin.site.register(Link, LinkAdmin)