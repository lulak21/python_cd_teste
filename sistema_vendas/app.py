from flask import Flask, escape, request

from sistema_vendas.calculadora_comissao import CalculadoraComissao

app = Flask(__name__)

@app.route('/comissao/<float:venda>')
def comissao(venda):
    return '{:.2f}'.format(CalculadoraComissao.calcular(venda))