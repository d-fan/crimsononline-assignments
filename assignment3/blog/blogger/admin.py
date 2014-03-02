from django.contrib import admin
from blogger.models import BlogPost, Author

class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'post', 'time', 'author']

admin.site.register(BlogPost, BlogPostAdmin)
# admin.site.register(BlogPost)
admin.site.register(Author)
