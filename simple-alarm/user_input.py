# noinspection PyGlobalUndefined
from datetime import datetime

def set_alarm(hour: str, minutes: str) -> str:
    if eval(hour) > 23:
        hour = eval(datetime.today().strftime('%H')) + 1

    if eval(minutes) > 59 or eval(minutes) == 60:
        minutes = datetime.today().strftime('%M')

    return f'{hour}:{minutes}'

