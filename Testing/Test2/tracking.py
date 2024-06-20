# tracking.py
def on_tracking_event(event):
    try:
        with event.device.open():
            info = event.device.get_info()
    except Exception:  # Catching a generic exception for mock purposes
        info = event.device.get_info()

    print(f"Found device {info}")

    for hand in event.hands:
        attributes = dir(event)
        for attribute in attributes:
            if not attribute.startswith('__'):
                value = getattr(event, attribute)
                print(f"{attribute}: {value}")
        hand_type = "left" if str(hand.type) == "HandType.Left" else "right"
        print(f"The hand type is {hand_type}.")
