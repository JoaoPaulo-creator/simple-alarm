# noinspection PyGlobalUndefined
def set_alarm(hour: str, minutes: str) -> str:
    if eval(hour) > 24:
        hour = '00'

    if eval(minutes) > 59:
        minutes = '00'

    return f'{hour}:{minutes}'

