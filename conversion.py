from forex_python.converter import CurrencyRates, CurrencyCodes


def converter(curr_1, curr_2, amnt):
    '''Converts the amount of one currency code to another.

    Parameters
    ----------
    :curr_1: str
        currency to convert from
    :curr_2: str
        currency to convert to
    :amnt: str
        amount to convert

    Returns
    -------
    float
        converted amount in correct currency

    >>> converter('USD', 'USD', 1)
    1.0
    '''

    cr = CurrencyRates()

    return cr.convert(curr_1, curr_2, float(amnt))


def get_symbol(code):
    '''Gets currency symbol.

    Parameters
    ----------
    :code: str

    Returns
    -------
    str
        currency symbol

    >>> get_symbol('USD')
    'US$'
    '''

    cc = CurrencyCodes()

    return cc.get_symbol(code)
