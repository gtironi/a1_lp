import data_analisy as da
import unittest
import pandas as pd

class TestMeasureTendency(unittest.TestCase):
    def test_numeric_column(self):          # teste coluna numérica
        data = pd.DataFrame({'Coluna1': [5, 7, 8, 9, 10, 10]})
        result = da.measure_tendency(data, 'Coluna1')
        self.assertEqual(result, (8.167, 8.5, 10))

    def test_categorical_column(self):      # teste coluna categórica
        data = pd.DataFrame({'Coluna2': ['A', 'B', 'A', 'C', 'B', 'A']})
        result = da.measure_tendency(data, 'Coluna2')
        self.assertEqual(result, 'A')


class TestMeasureDispersion(unittest.TestCase):
    def test_numeric_column(self):      # teste para coluna numérica
        data = pd.DataFrame({'Coluna1': [5, 7, 8, 9, 10, 10]})
        result = da.measure_dispersion(data, 'Coluna1')
        self.assertEqual(result, (1.941, 3.767, 10, 5, 5))
 
    def test_categorical_column(self):      # teste coluna categórica 
        data = pd.DataFrame({'Coluna2': ['A', 'B', 'A', 'C', 'B', 'A']})
        result = da.measure_dispersion(data, 'Coluna2')
        self.assertEqual(result, ())



if __name__ == '__main__':
    unittest.main()