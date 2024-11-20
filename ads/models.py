from django.db import models

from config.settings import AUTH_USER_MODEL


class Ad(models.Model):
    """ Модель объявления. """
    title = models.CharField(max_length=150, verbose_name='название товара')
    price = models.IntegerField(default=0, verbose_name='стоимость товара')
    description = models.TextField(verbose_name='описание товара')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания объявления')

    def __str__(self):
        return f"{self.title} - {self.price}: author {self.author}"

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Review(models.Model):
    """ Модель отзыва. """
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания отзыва')

    def __str__(self):
        return f'{self.ad} - {self.text}: author {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
