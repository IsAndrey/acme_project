from datetime import date


def get_birthday_for_year(birthday: date, year: int) -> date:
    """День рожденья в выбранном году"""
    try:
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        calculated_birthday = date(year=year, month=3, day=1)
        print(ValueError)
    return calculated_birthday
        

def calculate_birthday_countdown(birthday: date) -> int:
    """Расчет дней до дня рожденья"""
    today = date.today()
    this_year_birthday = get_birthday_for_year(
        birthday=birthday,
        year=today.year
    )
    if today > this_year_birthday:
        next_birthday = get_birthday_for_year(
            birthday=birthday,
            year=today.year+1
        )
    else:
        next_birthday = this_year_birthday
    birthday_countdown = (next_birthday-today).days
    return birthday_countdown
