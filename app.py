from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from conversion import converter, get_symbol
from forms import ConversionForm

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'sercretkey'
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'sketchy'


@app.route('/')
def redirect_index():
    '''Redirects to form'''
    return redirect(url_for('convert'))


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    '''Render index page with currency conversion form.'''

    form = ConversionForm()

    if form.validate_on_submit():
        curr1 = form.curr_from.data.upper()
        curr2 = form.curr_to.data.upper()
        amount = form.amount.data

        total = '{:.2f}'.format(converter(curr1, curr2, amount))
        symbol = get_symbol(curr2)

        return redirect(url_for('show_results', sym=symbol, total=total))

    return render_template('index.html', form=form)


@app.route('/results')
def show_results():
    '''Show the results page.'''

    sym = request.args.get('sym')
    total = request.args.get('total')

    return render_template('results.html', total=total, symbol=sym)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
