from django.urls import path, include

from app import views

app_name = "app"
urlpatterns = [
    path("", views.blog_posts, name="posts"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("post/create", views.blog_create, name="blog_create"),
    path("categories/<category>/", views.blog_category, name="blog_category"),
    path("like/<int:pk>", views.blog_like, name="blog_like"),
    path("about/", views.blog_about, name="blog_about"),
    path("contacts/", views.blog_contacts, name="blog_contacts"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup", views.blog_signup, name="blog_signup")
]
