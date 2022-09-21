from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def pagina_de_clientes():
    
    clientes = [
        {
            'nome': 'Luan Fonseca de Farias',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Angela Lucia',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Sandra de Sá',
            'email': 'email@exemplo.com'
        }, 
        {
            'nome': 'Rita de Cassia',
            'email': 'rita@exemplo.com'
        }
    ]
    return render_template('clientes.html', clientes=clientes)

@app.route("/transacoes")
def pagina_de_transacoes():
    cliente = {
        "nome": "Luan Fonsceca de Farias",
        "email": " email@exemplo.com",
        "telefone": " (99) 9 9999-9999"
    }

    transacoes= [
        {
            'id': '#9999',
            'data': '99/99/9999',
            'valor': 'R$99,99'

        }, 
        {
            'id': '#9999',
            'data': '99/99/9999',
            'valor': 'R$99,99'

        }, 
        {
            'id': '#9999',
            'data': '99/99/9999',
            'valor': 'R$99,99'
        }, 
        {
            'id': '#9999',
            'data': '99/99/9999',
            'valor': 'R$99,99'
        }
]
    return render_template('transacoes.html', cliente=cliente, transacoes= transacoes)



if __name__ == '__main__':
    app.run(debug=True)    