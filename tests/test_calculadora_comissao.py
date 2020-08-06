#Lula
#Danilo
#Leandro
#Manoel
#Arthur
#Yuri
#Michelle
from unittest import TestCase
from sistema_vendas.calculadora_comissao import CalculadoraComissao

class TestCalculadoraComissao(TestCase):

    def test_calcula_venda_10000_retorna_comissao_500(self):
        # arrange
        valor_venda = 10000.00
        valor_comissao = 500.00

        # act
        retorno = CalculadoraComissao.calcular(valor_venda)

        # assert
        self.assertEqual(valor_comissao, retorno)

    def test_calcula_venda_1555_59_retorna_comissao_77_77(self):
        # arrange
        valor_venda = 1555.59
        valor_comissao = 77.77

        # act
        retorno = CalculadoraComissao.calcular(valor_venda)

        # assert
        self.assertEqual(valor_comissao, retorno)

    def test_calcula_venda_20000_retorna_comissao_1200(self):
        # arrange
        valor_venda = 20000.00
        valor_comissao = 1200.00

        # act
        retorno = CalculadoraComissao.calcular(valor_venda)

        # assert
        self.assertEqual(valor_comissao, retorno)

    def test_calcula_venda_5000_retorna_comissao_250(self):
        # arrange
        valor_venda = 5000.00
        valor_comissao = 250.00

        # act
        retorno = CalculadoraComissao.calcular(valor_venda)

        # assert
        self.assertEqual(valor_comissao, retorno)