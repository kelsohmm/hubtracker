from datetime import timedelta, date


def shift_date(date, days_to_shift):
    return date + timedelta(days_to_shift)

def is_date_valid(year, month, day):
    try:
        date(year, month, day)
        return True
    except:
        return False