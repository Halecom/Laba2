from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name="Имя пользователя")
    password = models.CharField(max_length=255, verbose_name="Пароль")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
