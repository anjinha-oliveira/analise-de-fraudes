from flask import Flask
from flask import render_template
import pyodbc

app = Flask(__name__)

dados_de_conexao = (
                    "Driver={SQL Server};"
                    "Server=BRENO-LAPTOP;"
                    "Database=Fraudes;"
                    )
conexao = pyodbc.connect(dados_de_conexao)
cursor = conexao.cursor()

@app.route("/")
def pagina_de_clientes():
    query_clientes_fraudulentos = """
        SELECT 
            distinct cliente_id AS id, clientes.nome, clientes.email
        FROM transacoes AS t1
        inner join clientes
        on t1.cliente_id = clientes.ID
            WHERE t1.id in
                (SELECT
                    t1.ID
                FROM
                    transacoes t2
                where
                    t1.cliente_id = t2.cliente_id and
                    t1.ID != t2.ID and 
                    DATEDIFF(MINUTE, t1.data, t2.data) < 2 and t2.data < t1.data
                )
    """
    cursor.execute(query_clientes_fraudulentos)
    clientes = cursor.fetchall()
    print(clientes)
    return render_template('clientes.html', clientes=clientes)


@app.route("/transacoes/<cliente_id>")
def pagina_de_transacoes(cliente_id):
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