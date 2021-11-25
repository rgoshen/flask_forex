from flask import Flask, render_template, request, redirect, session
from currency_rates import get_currency_symbol, convert_currency
from helpers import get_cookies, set_cookies, handle_all


app = Flask(__name__)

app.config['SECRET_KEY'] = 'somethingsecret'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["TESTING"] = True


@app.route("/")
def get_form():
    set_cookies()
    return render_template("index.html")


@app.route('/convert', methods=['GET', 'POST'])
def get_currency_converted():
    if request.method == "POST":

        from_curr = request.form.get('from')
        to_curr = request.form.get('to')
        amount = request.form.get('amount')
        to_sym = get_currency_symbol(to_curr)

        get_cookies(from_curr, to_curr, amount)

        from_currency, to_currency, amount_ = handle_all(
            from_curr, to_curr, amount)
        if from_currency and to_currency and amount_:
            result = '{:.2f}'.format(convert_currency(
                from_currency, to_currency, amount_))
            session.clear()
            return render_template('result.html', result=result, to_sym=to_sym)

    return redirect('/')
