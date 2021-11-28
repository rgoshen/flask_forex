from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import ValidationError
from validators import code_check, amount_check


class ConversionForm(FlaskForm):
    '''Form to input currency codes and amount to convert.'''

    curr_from = StringField('Convert from', [code_check])
    curr_to = StringField('Convert to', [code_check])
    amount = FloatField('Amount', [amount_check])
    submit = SubmitField('Convert')


# class ResultsForm(FlaskForm):
#     '''Form to show the results of conversion.'''

#     results = StringField('Results')
#     submit = SubmitField('Home')
