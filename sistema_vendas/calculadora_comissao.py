import math

class CalculadoraComissao(object):

    @classmethod
    def calcular(cls, valor_venda):
        if valor_venda > 10000:
            return valor_venda * 6 / 100
        else:
            comissao = valor_venda * 5 / 100
            # 123,456
            # (vezes 100) 12345,6
            # (trunc) 12345
            # (dividido por 100) 123,45
            return math.trunc(comissao * 100) / 100