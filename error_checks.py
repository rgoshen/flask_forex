from flask import flash, session
from forex_python.converter import CurrencyRates


def check_valid_amount(val):
    '''Checking for a valid value.  Returns ValueError if not valid else returns val.'''

    if not val or not val.isnumeric():
        raise ValueError('Not a valid amount')

    return val


def check_valid_code(code):
    '''Checks for a valid code. Returns ValueError if not valid else returns code.'''

    cr = CurrencyRates()
    code = code.upper()

    # if USD it is a valid code
    if(code == 'USD'):
        return code

    all_currencies = list(cr.get_rates('USD').keys())

    if(not code or code not in all_currencies):
        raise ValueError('Not a valid code' + code)

    return code


def handel_errors(val, checker, key):
    try:
        checked = checker(val)
        return checked
    except ValueError as err:
        session[key]['valid'] = 'border border-danger'
        flash(str(err), 'error')
    return None
