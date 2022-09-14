import controller as c
print('Для сложения введите "+"\n'
      'Для вычитание введите "-"\n'
      'Для умножение введите "*"\n'
      'Для деление введите "/"\n'
      'Для возведение в степерь введите "^"')
x = True
while x:
    choice = input('\nВведите нужную операцию = ')
    if choice == '+':
        c.button_add()
    if choice == '-':
        c.button_diff()
    if choice == '*':
        c.button_mult()
    if choice == '/':
        c.button_div()
    if choice == '^':
        c.button_power()
    if choice == 'exit':
        x = False
