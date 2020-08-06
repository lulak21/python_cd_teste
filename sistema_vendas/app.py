from flask import Flask, escape, request

from .calculadora_comissao import CalculadoraComissao

app = Flask(__name__)

@app.route('/comissao/<float:valor_venda>')
def comissao(venda):
    return f'{CalculadoraComissao.calcular(valor_venda)}'
