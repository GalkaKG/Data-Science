import unittest
import sys
import os
import pandas as pd

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_preprocessing import load_data, clean_data, scale_data


# from src.data_preprocessing import load_data, clean_data, scale_data


class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        })

    def test_load_data(self):
        # Mock data loading function
        # Assume load_data is properly implemented
        test_file_path = 'test_data.csv'
        self.df.to_csv(test_file_path, index=False)
        df_loaded = load_data(test_file_path)
        pd.testing.assert_frame_equal(self.df, df_loaded)
        
    def test_clean_data(self):
        # Test cleaning function
        # Assume clean_data drops any rows with NaN values
        df_with_nan = self.df.copy()
        df_with_nan.loc[2, 'A'] = None
        cleaned_df = clean_data(df_with_nan)
        self.assertNotIn(None, cleaned_df['A'].values)
        
    def test_scale_data(self):
        # Test scaling function
        scaled_df = scale_data(self.df)
        # Check if the scaling has been applied
        self.assertTrue((scaled_df['A'] >= 0).all())  # Example assertion, modify as needed
        self.assertTrue((scaled_df['B'] >= 0).all())
        self.assertTrue((scaled_df['C'] >= 0).all())

if __name__ == '__main__':
    unittest.main()
