import math
import logger
import view
import rational_calc

value_x = 0
value_y = 0


def init_values():
    global value_x
    global value_y
    value_x = view.get_value()
    value_y = view.get_value()


def init_value():
    global value_x
    value_x = view.get_value()


def button_add(result):
    rational_calc.init(value_x, value_y)
    result = rational_calc.add()
    return result


def button_diff(result):
    rational_calc.init(value_x, value_y)
    result = rational_calc.diff()
    return result


def button_mult(result):
    rational_calc.init(value_x, value_y)
    result = rational_calc.mult()
    return result


def button_div(result):
    rational_calc.init(value_x, value_y)
    result = rational_calc.div()
    return result


def button_power(result):
    rational_calc.init(value_x, value_y)
    result = rational_calc.power()
    return result


def button_sqrt(result):
    rational_calc.init_value(value_x)
    result = math.sqrt(value_x)
    return result


# метод для вывода меню
def menu():
    global message
    message = ('Для сложения введите "+"\n'
               'Для вычитание введите "-"\n'
               'Для умножение введите "*"\n'
               'Для деление введите "/"\n'
               'Для извлечения корня введите "sqrt"\n'
               'Для возведение в степерь введите "^"')
    print(message)


def run():
    menu()
    x = True
    while x:
        choice = input('\nВведите нужную операцию = ')
        if choice == '+':
            init_values()
            button_add(result='')
            print(f"Ваш результат {button_add(result='')}")
            logger.log(f"{value_x} {choice} {value_y} ", button_add(result=''))
        if choice == '-':
            init_values()
            button_diff(result='')
            print(f"Ваш результат {button_diff(result='')}")
            logger.log(f"{value_x} {choice} {value_y} ", button_diff(result=''))

        if choice == '*':
            init_values()
            button_mult(result='')
            print(f"Ваш результат {button_mult(result='')}")
            logger.log(f"{value_x} {choice} {value_y} ", button_mult(result=''))
        if choice == '/':
            init_values()
            button_div(result='')
            print(f"Ваш результат {button_div(result='')}")
            logger.log(f"{value_x} {choice} {value_y} ", button_div(result=''))
        if choice == '^':
            init_values()
            button_power(result='')
            print(f"Ваш результат {button_power(result='')}")
            logger.log(f"{value_x} {choice} {value_y} ", button_power(result=''))
        if choice == 'sqrt':
            init_value()
            button_sqrt(result='')
            print(f"Ваш результат = {(button_sqrt(result=''))}")
            logger.log(f"{choice} {value_x} ", button_sqrt(result=''))
        if choice == 'help':
            menu()
            logger.log(f"{choice}", message)
        if choice == 'exit':
            logger.log(f"{choice}", 'Выход с приложения')
            x = False
