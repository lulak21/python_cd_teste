import math

class CalculadoraComissao(object):

    @classmethod
    def calcular(cls, valor_venda):
        if valor_venda > 10000:
            return valor_venda * 0.06
        else:
            comissao = valor_venda * 0.05
            # 123,456
            # (vezes 100) 12345,6
            # (dividido por 100) 123,45
            return math.floor(comissao * 100) / 100