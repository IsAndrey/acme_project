from django.db import models
from django.urls import reverse
# from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import real_age


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
        blank=False,
        validators=(real_age,)
    )
    image = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='birthdays_images'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'second_name', 'birthday'),
                name='Uniqie person constraint',
            ),
        )
    
    def get_absolute_url(self):
        return reverse('birthday:new_detail', kwargs={'pk':self.pk})
