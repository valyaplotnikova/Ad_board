from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя. """

    ROLE = {'user': 'user',
            'admin': 'admin'}

    username = None
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия пользователя')
    phone = models.CharField(max_length=11, **NULLABLE, verbose_name='Телефон пользователя')
    email = models.EmailField(unique=True, verbose_name='Email')
    role = models.CharField(max_length=11, choices=ROLE, default='user', verbose_name='Роль пользователя в системе')
    image = models.ImageField(upload_to='users/image/', **NULLABLE, verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


