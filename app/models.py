from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    likes = models.IntegerField(default=0, null=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

class About(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name_plural = "about"

class Contacts(models.Model):
    phone = models.TextField()
    email = models.TextField()
    address = models.TextField()

    class Meta:
        verbose_name_plural = "contacts"
