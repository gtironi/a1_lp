import unittest
import data_cleaner as dc

class TesteCsvToDataframe(unittest.TestCase):
    #Normal Test
    def test_input_value_type(self):
        self.assertRaises(ValueError, dc.csv_to_dataframe, 2)
    # Data Type Checking





if __name__ == "__main__":
    unittest.main()