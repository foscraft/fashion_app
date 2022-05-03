#from werkzeug import abort
from flask import Blueprint, render_template,abort
from c_app.product.models import PRODUCTS

fashion = Blueprint('fashion', __name__)

@fashion.route('/')
@fashion.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@fashion.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)