import sys
sys.path.insert(1,"./")
import unittest
import pandas as pd
from data_work.get_data_ready import *

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Idade': [25, 30, 35, 25, 40],
    'Cidade': ['Nova Iorque', 'Los Angeles', 'Chicago', 'Nova Iorque', 'Boston'],
    'Salario': [55000, 60000, None, 45000, 70000]
}

df_test = pd.DataFrame(data)

class TestGetDataReady(unittest.TestCase):

    def setUp(self):
        data = {
            'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Idade': [25, 30, 35, 25, 40],
            'Cidade': ['Nova Iorque', 'Los Angeles', 'Chicago', 'Nova Iorque', 'Boston'],
            'Salario': [55000, 60000, None, 45000, 70000]
        }
        self.df_test = pd.DataFrame(data)

    def test_limitar_respostas_diferentes(self):
        coluna_limites = {'Nome': 3, 'Cidade': 2}
        limitar_respostas_diferentes(self.df_test, coluna_limites)
        self.assertEqual(self.df_test['Nome'].nunique(), 3)
        self.assertEqual(self.df_test['Cidade'].nunique(), 2)

    def test_remover_linhas_com_valores_em_branco(self):
        colunas_a_verificar = ['Nome', 'Idade', 'Cidade', 'Salario']
        remover_linhas_com_valores_em_branco(self.df_test, colunas_a_verificar)
        self.assertTrue(self.df_test['Salario'].isna().sum() == 0)

    def test_tratar_tipo_dados(self):
        tipos_validos = [int, str]
        tratar_tipo_dados(self.df_test, tipos_validos)
        self.assertTrue(self.df_test['Idade'].dtype == "object")
        self.assertTrue(self.df_test['Cidade'].dtype == "object")

if __name__ == '__main__':
    unittest.main()
