from forex_python.converter import CurrencyRates
from wtforms.validators import ValidationError

cr = CurrencyRates()


def code_check(form, field):
    '''Custom code validator.
    Raises ValidationError if empty, code length is not 3 characters, not in uppercase or not in the list.
    '''

    if not field.data:
        raise ValidationError('Please provide a currency code')

    if len(field.data) != 3:
        raise ValidationError('Code must be 3 characters')

    if not field.data.isupper():
        raise ValidationError('Please provide all caps')

    # all currency rates codes
    rates = cr.get_rates('')

    if field.data not in rates:
        raise ValidationError('Invalid code')


def amount_check(form, field):
    '''Custom code validator.
    Raises ValidationError if empty or negative value.
    '''
    if not field.data:
        raise ValidationError('Please provide an amount')

    if field.data < 0:
        raise ValidationError("Please provide a positive value")
