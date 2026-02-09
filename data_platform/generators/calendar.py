from datetime import date, timedelta


def generate_dates(days: int = 30):
    """
    Генерирует список дат за последние n дней
    """
    today = date.today()
    return [today - timedelta(days=i) for i in range(days)]