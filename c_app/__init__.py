from flask import Flask
from c_app.product.views import fashion

app = Flask(__name__)
app.register_blueprint(fashion)