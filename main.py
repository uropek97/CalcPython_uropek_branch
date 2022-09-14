from unittest import result

import controller
import controller as c
import logger
import logger as l
import rational_calc
import view

controller.run()
x = True
while x:
    choice = input('\nВведите нужную операцию = ')
    if choice == '+':
        c.button_add()
        logger.log({choice}, )
    if choice == '-':
        c.button_diff()
        logger.log({choice}, 'test')
    if choice == '*':
        c.button_mult()
        logger.log({choice}, 'test')
    if choice == '/':
        c.button_div()
        logger.log({choice}, 'test')
    if choice == '^':
        c.button_power()
        logger.log({choice}, 'test')
    if choice == 'sqrt':
        c.button_sqrt()
        logger.log({choice}, 'test')
    if choice == 'exit':
        logger.log({choice}, 'test')
        x = False
