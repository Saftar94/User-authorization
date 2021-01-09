from django.db import models


# Create your models here.

class Name(models.Model):
    title = models.CharField('Login', max_length=250)
    password = models.CharField('password', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Arti(models.Model):
    title = models.CharField('Login', max_length=250)
    pasword = models.CharField('password', max_length=250)
    full_text = models.TextField('Cтатья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/intapp/{self.id}/newsdetail'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'