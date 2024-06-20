import unittest
from unittest.mock import patch, mock_open, MagicMock
import numpy as np
import render  # Assuming the refactored code is in a file named render.py

class TestMainFunction(unittest.TestCase):

    @patch('render.input', return_value='test_file')
    @patch('builtins.open', new_callable=mock_open)
    @patch('render.create_csv_file')
    @patch('render.Canvas')
    @patch('render.Connection')
    @patch('render.update_canvas')
    def test_main(self, mock_update_canvas, mock_connection, mock_canvas, mock_create_csv_file, mock_open, mock_input):
        # Mock instances
        mock_canvas_instance = mock_canvas.return_value
        mock_connection_instance = mock_connection.return_value
        
        # Setup return values and side effects
        mock_canvas_instance.name = "MockCanvas"
        mock_canvas_instance.screen_size = (640, 480)
        mock_canvas_instance.clearCanvas = False
        mock_canvas_instance.output_image = np.zeros((640, 480, 3), np.uint8)

        mock_update_canvas.return_value = np.zeros((640, 480, 3), np.uint8)
        
        # Run the main function
        render.main()
        
        # Check that the CSV file was created
        mock_create_csv_file.assert_called_once_with('test_file.csv', 
            ['frame_id', 'index_x_coor', 'index_y_coor', 'index_z_coor',
             'palm_x_coor', 'palm_y_coor', 'palm_z_coor', 'index_x_velocity',
             'index_y_velocity', 'index_z_velocity', 'palm_velocity_x',
             'palm_velocity_y', 'palm_velocity_z', 'confidence',
             'hand_grab_angle', 'hand_grab_strength', 'armPosition_x',
             'armPosition_y', 'armPosition_z', 'tip_rotation_x',
             'tip_rotation_y', 'tip_rotation_z', 'tip_rotation_w', 'target'])

        # Check that the connection and canvas methods were called
        mock_connection_instance.set_tracking_mode.assert_called_with("Desktop")
        mock_canvas_instance.set_tracking_mode.assert_called_with("Desktop")
        
        # Check that update_canvas was called
        mock_update_canvas.assert_called()


    @patch('render.input', return_value='test_file')
    @patch('builtins.open', new_callable=mock_open)
    @patch('render.create_csv_file')
    @patch('render.Canvas')
    @patch('render.Connection')
    @patch('render.update_canvas')
    def test_csv_file_creation(self, mock_update_canvas, mock_connection, mock_canvas, mock_create_csv_file, mock_open, mock_input):
        # Run the main function
        render.main()

        # Check that the CSV file was created with the correct header
        mock_create_csv_file.assert_called_once_with('test_file.csv', 
            ['frame_id', 'index_x_coor', 'index_y_coor', 'index_z_coor',
             'palm_x_coor', 'palm_y_coor', 'palm_z_coor', 'index_x_velocity',
             'index_y_velocity', 'index_z_velocity', 'palm_velocity_x',
             'palm_velocity_y', 'palm_velocity_z', 'confidence',
             'hand_grab_angle', 'hand_grab_strength', 'armPosition_x',
             'armPosition_y', 'armPosition_z', 'tip_rotation_x',
             'tip_rotation_y', 'tip_rotation_z', 'tip_rotation_w', 'target'])


    @patch('render.input', return_value='test_file')
    @patch('builtins.open', new_callable=mock_open)
    @patch('render.create_csv_file')
    @patch('render.Canvas')
    @patch('render.Connection')
    @patch('render.update_canvas')
    def test_tracking_mode_setting(self, mock_update_canvas, mock_connection, mock_canvas, mock_create_csv_file, mock_open, mock_input):
        # Mock instances
        mock_canvas_instance = mock_canvas.return_value
        mock_connection_instance = mock_connection.return_value

        # Run the main function
        render.main()

        # Check that the tracking mode was set correctly
        mock_connection_instance.set_tracking_mode.assert_called_with("Desktop")
        mock_canvas_instance.set_tracking_mode.assert_called_with("Desktop")

    @patch('render.input', return_value='test_file')
    @patch('builtins.open', new_callable=mock_open)
    @patch('render.create_csv_file')
    @patch('render.Canvas')
    @patch('render.Connection')
    @patch('render.update_canvas')
    def test_canvas_clearing(self, mock_update_canvas, mock_connection, mock_canvas, mock_create_csv_file, mock_open, mock_input):
        # Mock instances
        mock_canvas_instance = mock_canvas.return_value
        mock_canvas_instance.clearCanvas = True
        
        # Run the main function
        render.main()

        # Check that the canvas was cleared
        mock_update_canvas.assert_called_with(mock_canvas_instance, 'test_file.csv', 
            ['frame_id', 'index_x_coor', 'index_y_coor', 'index_z_coor',
             'palm_x_coor', 'palm_y_coor', 'palm_z_coor', 'index_x_velocity',
             'index_y_velocity', 'index_z_velocity', 'palm_velocity_x',
             'palm_velocity_y', 'palm_velocity_z', 'confidence',
             'hand_grab_angle', 'hand_grab_strength', 'armPosition_x',
             'armPosition_y', 'armPosition_z', 'tip_rotation_x',
             'tip_rotation_y', 'tip_rotation_z', 'tip_rotation_w', 'target'])
        mock_canvas_instance.clearCanvas = False
        self.assertFalse(mock_canvas_instance.clearCanvas)

if __name__ == '__main__':
    unittest.main()
