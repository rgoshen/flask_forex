from forex_python.converter import CurrencyCodes, CurrencyRates

cr = CurrencyRates()
cc = CurrencyCodes()

all_currencies = list(cr.get_rates('USD').keys())


def get_conversion_rate(from_curr, to_curr):
    '''Returns the conversion rate.'''
    return cr.get_rate(from_curr.upper(), to_curr.upper())


def get_currency_symbol(code):
    '''Returns the currency symbol.'''
    return cc.get_symbol(code.upper())


def convert_currency(from_curr, to_curr, amount=0):
    '''Returns the converted amount.'''
    return cr.convert(from_curr.upper(), to_curr.upper(), amount)
