from django.db import models

# Create your models here.


class Items(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(
        max_digits=7, decimal_places=0, verbose_name='Цена')
    photo = models.ImageField(upload_to="Items/", verbose_name='Промо товара')

    class Meta:
        verbose_name = 'Позиции'
        verbose_name_plural = 'Товары'


class Reg(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Зарегистрированные пользователи'


class Mail(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели рассылки'
