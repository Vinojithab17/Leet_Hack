import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import render  # Assuming the function is in a file named render.py

class TestVisualizeNormalizedVsNonNormalized(unittest.TestCase):

    @patch('render.pd.read_csv')
    @patch('render.plt.show')
    def test_visualize_normalized_vs_non_normalized(self, mock_show, mock_read_csv):
        # Mock CSV data
        csv_data = StringIO("""
        index_x_coor,index_y_coor,index_z_coor
        1,2,3
        4,5,6
        7,8,9
        """)
        
        # Mock DataFrame
        mock_df = pd.read_csv(csv_data)
        mock_read_csv.return_value = mock_df
        
        # Call the function with mock file paths
        file_paths = ['mock_file_1.csv', 'mock_file_2.csv']
        render.visualize_normalized_vs_non_normalized(file_paths)
        
        # Assert read_csv is called correctly
        calls = [patch('render.pd.read_csv').call(file_path) for file_path in file_paths]
        mock_read_csv.assert_has_calls(calls, any_order=True)
        
        # Assert plt.show() is called once
        mock_show.assert_called_once()

    @patch('render.pd.read_csv')
    def test_normalization(self, mock_read_csv):
        # Mock CSV data to check normalization
        csv_data = StringIO("""
        index_x_coor,index_y_coor,index_z_coor
        1,1,1
        2,2,2
        3,3,3
        """)
        
        # Expected normalized data
        normalized_data = {
            'index_x_coor': [-0.6666666666666666, 0.0, 0.6666666666666666],
            'index_y_coor': [-0.6666666666666666, 0.0, 0.6666666666666666],
            'index_z_coor': [-0.6666666666666666, 0.0, 0.6666666666666666]
        }
        
        # Mock DataFrame
        mock_df = pd.read_csv(csv_data)
        mock_read_csv.return_value = mock_df
        
        # Call the function with mock file path
        file_paths = ['mock_file_1.csv']
        render.visualize_normalized_vs_non_normalized(file_paths)
        
        # Calculate the normalization manually for verification
        centroid_x = mock_df['index_x_coor'].mean()
        centroid_y = mock_df['index_y_coor'].mean()
        centroid_z = mock_df['index_z_coor'].mean()

        mock_df['index_x_coor'] -= centroid_x
        mock_df['index_y_coor'] -= centroid_y
        mock_df['index_z_coor'] -= centroid_z

        max_distance = max(
            mock_df['index_x_coor'].max() - mock_df['index_x_coor'].min(),
            mock_df['index_y_coor'].max() - mock_df['index_y_coor'].min(),
            mock_df['index_z_coor'].max() - mock_df['index_z_coor'].min()
        )
        scale_factor = 10.0 / max_distance

        mock_df['index_x_coor'] *= scale_factor
        mock_df['index_y_coor'] *= scale_factor
        mock_df['index_z_coor'] *= scale_factor
        
        # Assert normalization is correct
        for key, values in normalized_data.items():
            for i, value in enumerate(values):
                self.assertAlmostEqual(mock_df[key].iloc[i], value, places=6)

if __name__ == '__main__':
    unittest.main()
