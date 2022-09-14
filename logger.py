from datetime import datetime


def log(expression, result):
    time = datetime.now().strftime('%d.%m.%y - %H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{time} {expression} = {result}')
