import view
import rational_calc


def button_add():
    value_x = view.get_value()
    value_y = view.get_value()
    rational_calc.init(value_x, value_y)
    result = rational_calc.add()
    view.view_data(result)


def button_diff():
    value_x = view.get_value()
    value_y = view.get_value()
    rational_calc.init(value_x, value_y)
    result = rational_calc.diff()
    view.view_data(result)


def button_mult():
    value_x = view.get_value()
    value_y = view.get_value()
    rational_calc.init(value_x, value_y)
    result = rational_calc.mult()
    view.view_data(result)


def button_div():
    value_x = view.get_value()
    value_y = view.get_value()
    rational_calc.init(value_x, value_y)
    result = rational_calc.div()
    view.view_data(result)


def button_power():
    value_x = view.get_value()
    value_y = view.get_value()
    rational_calc.init(value_x, value_y)
    result = rational_calc.power()
    view.view_data(result)
