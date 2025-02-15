import unittest
import pandas as pd
from src.data.preprocessing import clean_data

class TestDataProcessing(unittest.TestCase):
    def test_clean_data(self):
        df = pd.DataFrame({'col1': [1, 2, None], 'col2': [3, None, 4]})
        cleaned_df = clean_data(df)
        self.assertEqual(cleaned_df.isnull().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()
