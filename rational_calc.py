# модуль для работы с рациональными числами
x = 0
y = 0


# фунцкия для инициализации значении
def init(a, b):
    global x
    global y
    x = a
    y = b


add = lambda: x + y  # сложение значений
diff = lambda: x - y  # вычитание значений
mult = lambda: x * y  # умножение значений
div = lambda: x / y  # деление значений
power = lambda: x ** y  # возведение в степерь значений
