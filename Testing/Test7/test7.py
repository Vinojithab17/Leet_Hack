import unittest
from unittest.mock import patch, MagicMock
import cv2
import numpy as np
import main  # Assuming the main function is in a file named main.py

class TestMainFunction(unittest.TestCase):

    @patch('cv2.imshow')
    @patch('cv2.waitKey', return_value=0xFF)
    @patch('cv2.destroyAllWindows')
    @patch('main.Canvas')
    def test_main(self, mock_canvas_cls, mock_destroyAllWindows, mock_waitKey, mock_imshow):
        # Mock instances
        mock_canvas_instance = MagicMock(spec=main.Canvas)
        mock_canvas_instance.screen_size = (640, 480)
        mock_canvas_instance.clearCanvas = False
        mock_canvas_instance.drawingMode = True
        mock_canvas_instance.position = (0, 0)
        mock_canvas_instance.name = "Canvas"
        
        # Set the output_image attribute to return a numpy array
        mock_canvas_instance.output_image = np.zeros((640, 480, 3), np.uint8)
        mock_canvas_cls.return_value = mock_canvas_instance

        # Run the main function
        main.main()

        # Assertions
        mock_canvas_cls.assert_called_once()
        self.assertTrue(mock_canvas_instance.set_tracking_mode.called)
        self.assertTrue(mock_imshow.called)
        self.assertTrue(mock_waitKey.called)
        self.assertTrue(mock_destroyAllWindows.called)

if __name__ == '__main__':
    unittest.main()
