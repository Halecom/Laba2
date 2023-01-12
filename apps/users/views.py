from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.users import forms
from apps.users.models import User


def register(request):
    if request.session.get("user_id"):
        return HttpResponseRedirect("/posts/")

    form = forms.RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        request.session["user_id"] = user.id
        return HttpResponseRedirect("/posts/")

    return render(request, "users/registration.html", {"form": form})


def authorization(request):
    if request.session.get("user_id"):
        return HttpResponseRedirect("/posts/")

    form = forms.AuthorizationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        try:
            user = User.objects.get(username=form.data["username"])
        except User.DoesNotExist:
            form.add_error("username", "Такой пользователь не существует!")
        else:
            if user.password != form.data["password"]:
                form.add_error("password", "Неверный пароль!")
            else:
                request.session["user_id"] = user.id
                return HttpResponseRedirect("/posts/")

    return render(request, "users/authorization.html", {"form": form})


def logout(request):
    request.session.pop("user_id")
    return HttpResponseRedirect("/posts/")
