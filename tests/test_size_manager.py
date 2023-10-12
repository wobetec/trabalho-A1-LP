import sys
import unittest
from numpy import save
import pandas as pd

sys.path.insert(1, "./")

from data_work.size_manager import *

df_test = pd.DataFrame(
    {
        "Nome": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Idade": [25, 30, 35, 28, 22],
        "Cidade": [
            "Nova York",
            "Los Angeles",
            "Chicago",
            "San Francisco",
            "Miami",
        ],
    }
)


class TestSizeManager(unittest.TestCase):
    def test_path_to(self):
        path_example = "data/teste.csv"
        self.assertEqual(
            path_to("teste", "csv")[-len(path_example) :], "data/teste.csv"
        )

    def test_crop_data(self):
        df_cropped = crop_data(df_test, ["Nome", "Idade"])
        self.assertEqual(df_cropped.columns.tolist(), ["Nome", "Idade"])

    def test_save_data(self):
        save_data(df_test, "teste_1")
        self.assertTrue(os.path.exists(path_to("teste_1", "csv")))

    def test_zip_file(self):
        zip_file("teste_2")
        self.assertTrue(os.path.exists(path_to("teste_2", "zip")))

    def test_unzip_file(self):
        unzip_file("teste_3")
        self.assertTrue(os.path.exists(path_to("teste_3", "csv")))

    def test_load_data(self):
        df = load_data("teste_2")
        self.assertTrue(isinstance(df, pd.DataFrame))

    @classmethod
    def tearDownClass(cls):
        os.remove(path_to("teste_1", "csv"))
        os.remove(path_to("teste_2", "zip"))
        os.remove(path_to("teste_3", "csv"))

if __name__ == "__main__":
    unittest.main()
