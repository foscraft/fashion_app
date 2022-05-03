from locale import currency
import ccy
from flask import Flask, request
from c_app.product.views import fashion

app = Flask(__name__)
app.register_blueprint(fashion)

@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return f'{currency_code} {amount}'
