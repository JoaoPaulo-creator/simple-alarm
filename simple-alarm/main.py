from pygame import mixer
from time import sleep
from datetime import datetime
from constants.constants import PATH_TO_MP3_FILE
from user_input import set_alarm


def play_alarm():
    path_to_file = PATH_TO_MP3_FILE
    mixer.init()
    sound = mixer.Sound(path_to_file)
    sound.play()
    sleep(10)


def main():
    while True:

        try:
            current_clock_hour = datetime.today().strftime('%H:%M')
            hour = str(input(': '))
            minutes = str(input(': '))
            alarm = set_alarm(hour, minutes)

            if current_clock_hour == alarm:
                print(alarm)
                play_alarm()
                print('='*20)
                print('Alarm is ringing')
                print('=' * 20)

            stop_alarm = str(input('Stop alarm? [S] [N]'))
            if stop_alarm.upper() == 'S':
                break

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    SystemExit(main())
