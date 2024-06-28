from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import Post, Comment, About, Contacts
from app.forms import CommentForm, CreateForm, SignUpForm

def blog_posts(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "base.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "detail.html", context)

def blog_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes += 1
    post.save()

    return redirect("app:blog_detail", pk=pk)

def blog_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.categories.set(form.cleaned_data["categories"])
            return redirect("app:blog_detail", pk=post.pk)

    context = {
        'form': CreateForm()
    }
    return render(request, "create.html", context)

def blog_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def blog_about(request):
    content = About.objects.first()
    return render(request, "about.html", { "about": content })

def blog_contacts(request):
    content = Contacts.objects.first()
    return render(request, "contacts.html", { "contacts": content })
