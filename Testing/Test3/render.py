# render.py
def render_hands(event, drawingMode):
    for i in range(0, len(event.hands)):
        hand = event.hands[i]
        for index_digit in range(0, 5):
            digit = hand.digits[index_digit]
            for index_bone in range(0, 4):
                bone = digit.bones[index_bone]
                if hand.grab_strength == 1.0:
                    drawingMode[0] = False
                    x1, y1 = 0, 0
                    # return

                if drawingMode[0]:
                    frame_id = event.tracking_frame_id
                    palm_velocity = hand.palm.velocity
                    palm_position = hand.palm.position
                    arm_position = hand.arm.next_joint
                    fingertip_rotation = hand.index.distal.rotation
