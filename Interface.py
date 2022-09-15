# импорт нужных библиотек и классов
import math
import tkinter as tk
from decimal import Decimal
import logger

# Создание окна с задаными размерами и названием
mainWindow = tk.Tk()
mainWindow.geometry('400x300')
mainWindow.title("Калькулятор")

# Создание этикетки(текста) с позиционированием для первого числа
top_label = tk.Label(mainWindow, text="Введите первое число")
top_label.place(relx=0.5, rely=0.04, anchor='n')  # Позиционирование текста

# Создание окна для ввода значения с позиционированием для первого числа
first_entry = tk.Entry(mainWindow, width=20)
first_entry.place(relx=0.5, rely=0.13, anchor='n')  # Позиционирование окна ввода занчения

# Создание этикетки(текста) с позиционированием для второго числа
heading_label = tk.Label(mainWindow, text="Введите второе число")
heading_label.place(relx=0.5, rely=0.28, anchor='n')  # Позиционирование текста

# Создание окна для ввода значения с позиционированием для второго числа
second_entry = tk.Entry(mainWindow, width=20)
second_entry.place(relx=0.5, rely=0.37, anchor='n')  # Позиционирование окна ввода занчения

# Позиционирование текста
operation = tk.Label(mainWindow, text="Операция")
operation.place(relx=0.5, rely=0.5, anchor='n')

result_label = tk.Label(mainWindow, text="Ваш результат: ")
result_label.place(relx=0.5, rely=0.75, anchor='n')


# метод для сложения значений
def add():
    first = Decimal(first_entry.get())
    second = Decimal(second_entry.get())
    result = first + second
    result_label.config(text="Ваш результат сложения: " + str(result))  # вывод результата на экран
    logger.log(f'{first} + {second} =', result)  # запись в log.tx


# запуск функции  add() при нажатий кнопки
addition_button = tk.Button(text="+", command=lambda: add())
addition_button.place(relx=0.28, rely=0.58, anchor='n')


# метод для вычитания чисел
def minus():
    first = Decimal(first_entry.get())
    second = Decimal(second_entry.get())
    result = first - second
    result_label.config(text="Ваш результат вычитания: " + str(result))  # вывод результата на экран
    logger.log(f'{first} - {second} =', result)  # запись в log.tx


# запуск функции minus() при нажатий кнопки
minus_button = tk.Button(mainWindow, text="-", command=lambda: minus())
minus_button.place(relx=0.38, rely=0.58, anchor='n')


# метод для умножения чисел
def multiply():
    first = Decimal(first_entry.get())
    second = Decimal(second_entry.get())
    result = first * second
    result_label.config(text="Ваш результат умножения: " + str(result))  # вывод результата на экран
    logger.log(f'{first} * {second} =', result)  # запись в log.tx


# запуск функции multiply() при нажатий кнопки
mul_button = tk.Button(mainWindow, text="*", command=lambda: multiply())
mul_button.place(relx=0.48, rely=0.58, anchor='n')


# метод для деления чисел
def divide():
    first = Decimal(first_entry.get())
    second = Decimal(second_entry.get())
    result = first / second
    result_label.config(text="Ваш результат деления: " + str(result))  # вывод результата на экран
    logger.log(f'{first} / {second} =', result)  # запись в log.tx


# запуск функции divide () при нажатий кнопки
divide_button = tk.Button(mainWindow, text="/", command=lambda: divide())
divide_button.place(relx=0.58, rely=0.58, anchor='n')


# метод для определения корня числа
def sqrt():
    first = Decimal(first_entry.get())
    result = math.sqrt(first)
    result_label.config(text="Ваш результат извлечения корня: " + str(result))  # вывод результата на экран
    logger.log(f'Корень числа {first}  =', result)  # запись в log.tx


# запуск функции sqrt () при нажатий кнопки
sqrt_button = tk.Button(mainWindow, text="sqrt", command=lambda: sqrt())
sqrt_button.place(relx=0.70, rely=0.58, anchor='n')

mainWindow.mainloop()
