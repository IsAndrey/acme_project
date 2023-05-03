from datetime import date
from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age_days = (date.today - value).days
    min_age_days = 365
    max_age_days = 90 * 365 + 30 * 366
    if age_days < min_age_days or age_days > max_age_days:
        raise ValidationError(
            'Ожидается возраст от 1 года до 120 лет.'
        )
