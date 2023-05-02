from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        blank=False
    )
    second_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40,
        blank=True,
        help_text='Необязательное поле'
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        blank=False
    )
