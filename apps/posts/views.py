from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.posts import forms
from apps.posts.models import Post, Reaction
from apps.users.models import User


def index(request):
    if request.session.get("user_id"):
        if request.method == "POST":
            form = forms.PostForm(request.POST)
            user = User.objects.get(id=request.session.get("user_id"))
            Post.objects.create(user=user, content=form.data["content"])

            return HttpResponseRedirect("/posts/")

        posts = Post.objects.order_by("-date")[:100]
        return render(request, "posts/index.html", {"posts": posts, "form": forms.PostForm()})

    return HttpResponseRedirect("/users/authorization/")


def delete_post(request, post_id):
    if request.session.get("user_id"):
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.session.get("user_id"))

        if post.user == user:
            post.delete()

    return HttpResponseRedirect("/posts/")


def update_post(request, post_id):
    if request.session.get("user_id"):
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.session.get("user_id"))

        if post.user == user:
            if request.method == "POST":
                form = forms.PostForm(request.POST)
                post.content = form.data["content"]
                post.save()
            else:
                form = forms.PostForm({"content": post.content})
                return render(request, "posts/update.html", {"post": post, "form": form})

    return HttpResponseRedirect("/posts/")


def react(request, post_id, type):
    if request.session.get("user_id"):
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.session.get("user_id"))

        if Reaction.objects.filter(user=user, post=post).exists():
            Reaction.objects.filter(user=user, post=post).delete()

        Reaction.objects.create(user=user, post=post, type=type)

    return HttpResponseRedirect("/posts/")
