import unittest
from unittest.mock import MagicMock, patch
import tracking

class MockDevice:
    def open(self):
        return MagicMock()

    def get_info(self):
        return "Mock Device Info"

class MockEvent:
    def __init__(self, hands):
        self.device = MockDevice()
        self.hands = hands

class MockHand:
    def __init__(self, hand_type):
        self.type = hand_type

class TestOnTrackingEvent(unittest.TestCase):
    
    def test_on_tracking_event_with_device_info(self):
        mock_hand = MockHand("HandType.Left")
        event = MockEvent(hands=[mock_hand])

        with patch('builtins.print') as mocked_print:
            tracking.on_tracking_event(event)

            mocked_print.assert_any_call("Found device Mock Device Info")
            mocked_print.assert_any_call("The hand type is left.")

    def test_on_tracking_event_with_multiple_hands(self):
        mock_hand_left = MockHand("HandType.Left")
        mock_hand_right = MockHand("HandType.Right")
        event = MockEvent(hands=[mock_hand_left, mock_hand_right])

        with patch('builtins.print') as mocked_print:
            tracking.on_tracking_event(event)

            mocked_print.assert_any_call("Found device Mock Device Info")
            mocked_print.assert_any_call("The hand type is left.")
            mocked_print.assert_any_call("The hand type is right.")

    def test_on_tracking_event_device_error(self):
        mock_hand = MockHand("HandType.Right")
        event = MockEvent(hands=[mock_hand])

        with patch.object(MockDevice, 'open', side_effect=Exception("Cannot open device")), \
             patch('builtins.print') as mocked_print:
            tracking.on_tracking_event(event)

            mocked_print.assert_any_call("Found device Mock Device Info")
            mocked_print.assert_any_call("The hand type is right.")

if __name__ == '__main__':
    unittest.main()
