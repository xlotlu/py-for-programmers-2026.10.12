from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Salutare</p>"

@app.route("/locatzie")
def ruta_noua():
    return "<p>Aici este o altă pagină</p>"

@app.route("/undeva/<var>")
def undeva(var):
    return f"<p>Sunt o pagină dinamică chemată cu «{var}»!!</p>"


# se rulează cu
# flask --app d4_ex6_flask_decorator_example run --reload
