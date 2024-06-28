from django.contrib import admin
from app.models import Category, Comment, Post, About, Contacts

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on", "last_modified"]

class CommentAdmin(admin.ModelAdmin):
    pass

class AboutAdmin(admin.ModelAdmin):
    pass

class ContactsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contacts, ContactsAdmin)
