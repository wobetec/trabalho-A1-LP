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
        df_modificado = limitar_respostas_diferentes(self.df_test, coluna_limites)
        self.assertEqual(df_modificado['Nome'].nunique(), 3)
        self.assertEqual(df_modificado['Cidade'].nunique(), 2)

    def test_remover_linhas_com_valores_em_branco(self):
        colunas_a_verificar = ['Nome', 'Idade', 'Cidade', 'Salario']
        df_modificado = remover_linhas_com_valores_em_branco(self.df_test, colunas_a_verificar)
        self.assertTrue(df_modificado['Salario'].isna().sum() == 0)

    def test_tratar_tipo_dados(self):
        tipos_validos = [int, str]
        df_modificado = tratar_tipo_dados(self.df_test, tipos_validos)
        self.assertTrue(df_modificado['Idade'].dtype == int)
        self.assertTrue(df_modificado['Cidade'].dtype == str)

if __name__ == '__main__':
    unittest.main()
