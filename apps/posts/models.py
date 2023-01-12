from django.db import models

from apps.users.models import User


class Post(models.Model):
    content = models.TextField(verbose_name="Текст")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Пользователь",
    )

    def likes(self):
        return self.reactions.filter(type=Reaction.Type.like)

    def dislikes(self):
        return self.reactions.filter(type=Reaction.Type.dislike)

    def ellipsis(self):
        return self.reactions.filter(type=Reaction.Type.ellipsis)


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пользователь",
    )

    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
        null=True,
    )

    comment = models.ForeignKey(
        to="Comment",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Коммент",
        null=True,
    )


class Reaction(models.Model):
    class Type(models.TextChoices):
        like = "like", "👍"
        dislike = "dislike", "👎"
        ellipsis = "ellipsis", "..."

    type = models.CharField(
        max_length=255,
        choices=Type.choices,
        verbose_name="Тип",
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="reactions",
        verbose_name="Пользователь",
    )

    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="reactions",
        verbose_name="Пост",
        null=True,
    )

    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name="reactions",
        verbose_name="Коммент",
        null=True,
    )
