import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from dataframe_handler import DataFrameHandler

class TestDataFrameHandler(unittest.TestCase):

    @patch('dataframe_handler.datetime')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv(self, mock_to_csv, mock_datetime):
  
        mock_now = MagicMock()
        mock_now.strftime.return_value = '06.19.2024_12.00.00'
        mock_datetime.now.return_value = mock_now

       
        sample_data = {'frame_id': [1, 2, 3], 'target': [1, 1, 1]}
        df = pd.DataFrame(sample_data)

        
        frame_id_list = [2, 3]
        csv_file_path = 'sample_file'
        handler = DataFrameHandler(df, frame_id_list, csv_file_path)

        handler.save_dataframe_to_csv()

        
        expected_data = {'frame_id': [1, 2, 3], 'target': [1, 0, 0]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(handler.new_df, expected_df)

        mock_to_csv.assert_called_once_with('Signatures/updated_sample_file.csv', index=False)

    @patch('dataframe_handler.datetime')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv_empty_dataframe(self, mock_to_csv, mock_datetime):
        mock_now = MagicMock()
        mock_now.strftime.return_value = '06.19.2024_12.00.00'
        mock_datetime.now.return_value = mock_now

        df = pd.DataFrame(columns=['frame_id', 'target'])

        handler = DataFrameHandler(df, [1, 2, 3], 'sample_file')
        handler.save_dataframe_to_csv()

        pd.testing.assert_frame_equal(handler.new_df, df)
        mock_to_csv.assert_called_once_with('Signatures/updated_sample_file.csv', index=False)

    @patch('dataframe_handler.datetime')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv_empty_frame_id_list(self, mock_to_csv, mock_datetime):
        mock_now = MagicMock()
        mock_now.strftime.return_value = '06.19.2024_12.00.00'
        mock_datetime.now.return_value = mock_now

        df = pd.DataFrame({'frame_id': [1, 2, 3], 'target': [1, 1, 1]})

        handler = DataFrameHandler(df, [], 'sample_file')
        handler.save_dataframe_to_csv()

        expected_df = pd.DataFrame({'frame_id': [1, 2, 3], 'target': [1, 1, 1]})
        pd.testing.assert_frame_equal(handler.new_df, expected_df)
        mock_to_csv.assert_called_once_with('Signatures/updated_sample_file.csv', index=False)

    @patch('dataframe_handler.datetime')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv_no_matching_frame_ids(self, mock_to_csv, mock_datetime):
        mock_now = MagicMock()
        mock_now.strftime.return_value = '06.19.2024_12.00.00'
        mock_datetime.now.return_value = mock_now

        df = pd.DataFrame({'frame_id': [1, 2, 3], 'target': [1, 1, 1]})

        handler = DataFrameHandler(df, [4, 5], 'sample_file')
        handler.save_dataframe_to_csv()

        expected_df = pd.DataFrame({'frame_id': [1, 2, 3], 'target': [1, 1, 1]})
        pd.testing.assert_frame_equal(handler.new_df, expected_df)
        mock_to_csv.assert_called_once_with('Signatures/updated_sample_file.csv', index=False)

    @patch('dataframe_handler.datetime')
    @patch('pandas.DataFrame.to_csv')
    def test_save_dataframe_to_csv_missing_frame_id_column(self, mock_to_csv, mock_datetime):
        mock_now = MagicMock()
        mock_now.strftime.return_value = '06.19.2024_12.00.00'
        mock_datetime.now.return_value = mock_now

        df = pd.DataFrame({'target': [1, 1, 1]})

        handler = DataFrameHandler(df, [2, 3], 'sample_file')

        with self.assertRaises(KeyError):
            handler.save_dataframe_to_csv()

if __name__ == '__main__':
    unittest.main()
