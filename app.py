from flask import Flask, render_template, request, redirect
from currency_rates import get_currency_symbol, convert_currency

app = Flask(__name__)


@app.route("/")
def get_from():
    return render_template("index.html")


@app.route('/convert', methods=['GET', 'POST'])
def get_currency_converted():
    if request.method == "POST":
        from_currency = request.form.get('from')
        to_currency = request.form.get('to')
        amount = float(request.form.get('amount'))
        to_sym = get_currency_symbol(to_currency)
        result = '{:.2f}'.format(convert_currency(
            from_currency, to_currency, amount))
        return render_template('result.html', result=result, to_sym=to_sym)
    return redirect('/')
