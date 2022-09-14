from decimal import Decimal


# вывод результата операции
def view_data(data):
    print(f'Результат операции : {data}')


# Ввод значений
def get_value():
    return Decimal(input('Введите число = '))
