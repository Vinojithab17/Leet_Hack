import unittest
from unittest.mock import MagicMock
from render import render_hands

class MockBone:
    pass

class MockDigit:
    def __init__(self):
        self.bones = [MockBone() for _ in range(4)]

class MockHand:
    def __init__(self, grab_strength):
        self.grab_strength = grab_strength
        self.digits = [MockDigit() for _ in range(5)]
        self.palm = MagicMock()
        self.arm = MagicMock()
        self.index = MagicMock()

class MockEvent:
    def __init__(self, hands):
        self.hands = hands
        self.tracking_frame_id = 123

class TestRenderHands(unittest.TestCase):
    def test_render_hands_grab_strength_1(self):
        hand = MockHand(grab_strength=1.0)
        event = MockEvent(hands=[hand])
        drawingMode = [True]

        render_hands(event, drawingMode)

        self.assertFalse(drawingMode[0], "Expected drawingMode to be False when grab_strength is 1.0")

    def test_render_hands_grab_strength_not_1(self):
        hand = MockHand(grab_strength=0.5)
        event = MockEvent(hands=[hand])
        drawingMode = [True]

        render_hands(event, drawingMode)

        self.assertTrue(drawingMode[0], "Expected drawingMode to remain True when grab_strength is not 1.0")

    def test_render_hands_attributes_accessed(self):
        hand = MockHand(grab_strength=0.5)
        event = MockEvent(hands=[hand])
        drawingMode = [True]

        render_hands(event, drawingMode)

        hand.palm.velocity.assert_called_once()
        hand.palm.position.assert_called_once()
        hand.arm.next_joint.assert_called_once()
        hand.index.distal.rotation.assert_called_once()

if __name__ == '__main__':
    unittest.main()
