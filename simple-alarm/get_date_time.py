from datetime import datetime

def get_time():
    return datetime.today().strftime('%H:%M')

