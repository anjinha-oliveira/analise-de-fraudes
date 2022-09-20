from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def pagina_de_clientes():
    return render_template('clientes.html')