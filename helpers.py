from flask import session
from error_checks import handel_errors, check_valid_amount, check_valid_code


def set_cookies():
    defaults = {
        'val': '',
        'valid': ''
    }

    session.setdefault('curr_1', defaults)
    session.setdefault('curr_2', defaults)
    session.setdefault('amount', defaults)


def get_cookies(from_curr, to_curr, amount):
    session['curr_1'] = from_curr
    session['curr_2'] = to_curr
    session['amount'] = amount


def clear_styles():
    session['curr_1']['valid'] = ''
    session['curr_2']['valid'] = ''
    session['amount']['valid'] = ''


def handle_all(from_curr, to_curr, amount):
    from_currency = handel_errors(from_curr, check_valid_code, 'curr_1')
    to_currency = handel_errors(to_curr, check_valid_code, 'curr_2')
    amount = handel_errors(amount, check_valid_amount, 'amount')

    return from_currency, to_currency, amount
