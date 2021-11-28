from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request, jsonify
from conversion import converter, get_symbol
from forms import ConversionForm

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'sercretkey'
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'sketchy'

# from_code = 'INR'  # may leave blank
# to_code = 'USD'  # cannot leave blank
# amount = '1'

# check_code(from_code)
# check_code(to_code)
# check_amount(amount)

# conversion = converter(from_code, to_code, amount)
# symbol = get_symbol(to_code)

# print(symbol, '{:.2f}'.format(conversion))


@app.route('/', methods=['GET', 'POST'])
def show_index():
    '''Render index page with currency conversion form.'''

    form = ConversionForm()

    if form.validate_on_submit():
        curr_1 = form.curr_from.data
        curr_2 = form.curr_to.data
        amnt = form.amount.data
        return redirect(url_for('convert', curr1=curr_1, curr2=curr_2, amount=amnt))
    else:
        return render_template('index.html', form=form)


@app.route('/convert')
def convert():
    '''Converts the amount from one currency code
    to another.  Returns a float value for currency and returns the symbol string.
    '''

    curr1 = request.args.get('curr1')
    curr2 = request.args.get('curr2')
    amount = float(request.args.get('amount'))

    total = '{:.2f}'.format(converter(curr1, curr2, amount))
    symbol = get_symbol(curr2)

    return redirect(url_for('show_results', sym=symbol, total=total))


@app.route('/results')
def show_results():
    '''Show the results page.'''

    sym = request.args.get('sym')
    total = request.args.get('total')

    return render_template('results.html', total=total, symbol=sym)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
