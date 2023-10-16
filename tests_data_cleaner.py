import unittest
import pandas as pd
import data_cleaner as dc
import os
import numpy as np

class TestCSVToDataFrame(unittest.TestCase):
    def test_valid_csv(self):       # teste csv normal válido
        data = pd.DataFrame({'Coluna1': [10, 8, 10, 2]})
        data.to_csv('teste.csv', index=False)
        result = dc.csv_to_dataframe('teste.csv')
        os.remove('teste.csv')
        self.assertTrue(result.equals(data))

class TestRemoveColunasIrrelevantes(unittest.TestCase):    
    def test_remove_columns(self):          # teste padrão, com valores NaN
        data = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, np.NaN, 8, np.NaN],'C':[7, 3, np.NaN, 2],'D':[1, np.NaN, np.NaN, np.NaN]})
        result = dc.remove_colunas_irrelevantes(data, num_NaN_values=2)
        expected = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, np.NaN, 8, np.NaN],'C':[7, 3, np.NaN, 2]})
        self.assertTrue(result.equals(expected))

    def test_no_NaN(self): # teste sem valores NaN
        data = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, 1, 8, 4],'C':[7, 3, 4, 2],'D':[1, 2, 3, 4]})
        result = dc.remove_colunas_irrelevantes(data, num_NaN_values=2)
        expected = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, 1, 8, 4],'C':[7, 3, 4, 2],'D':[1, 2, 3, 4]})
        self.assertTrue(result.equals(expected))

class TestReplace88888Values(unittest.TestCase):
    def test_replace_values(self):  # teste padrão, com valores 8888 
        data = pd.DataFrame({'A':[88888, 4, 6, 9],'B':[3, np.NaN, 8, 88888],'C':['opa', 'ola', np.NaN, 'oi'],'D':[1, 1, 1, 1]})
        result = dc.replace_88888_values(data)
        expected = pd.DataFrame({'A':[9, 4, 6, 9],'B':[3, np.NaN, 8, 8],'C':['opa', 'ola', np.NaN, 'oi'],'D':[1, 1, 1, 1]})
        self.assertTrue(result.equals(expected))
    
    def test_replace_values(self):  # teste sem valores 8888
        data = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, np.NaN, 8, 9],'C':['opa', 'ola', np.NaN, 'oi'],'D':[1, 1, 1, 1]})
        result = dc.replace_88888_values(data)
        expected = pd.DataFrame({'A':[1, 4, 6, 9],'B':[3, np.NaN, 8, 9],'C':['opa', 'ola', np.NaN, 'oi'],'D':[1, 1, 1, 1]})
        self.assertTrue(result.equals(expected))

class TestCorrigeNomeEstados(unittest.TestCase):
    def test_correct_state_names(self):     # teste padrão, dataframe válido, com coluna NO_UF
        data = pd.DataFrame({'NU_ANO_CENSO': [2021, 2021, 2021], 'NO_UF': ['Rond⌠nia', 'Amapß', 'Maranhπo']})
        result = dc.corrige_nome_estados(data)
        expected = pd.DataFrame({'NU_ANO_CENSO': [2021, 2021, 2021], 'NO_UF': ['Rondônia', 'Amapá', 'Maranhão']})
        self.assertTrue(result.equals(expected))

if __name__ == "__main__":
    unittest.main()