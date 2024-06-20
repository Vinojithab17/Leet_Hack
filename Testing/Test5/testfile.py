import time
from threading import Event, Thread

# Mock classes and functions

class TrackingEventListener:
    pass

class MultiDeviceListener:
    def __init__(self, event_type):
        self.n_events = 0

class Connection:
    def __init__(self, multi_device_aware=False):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def open(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def wait_until(condition, timeout=5):
    end_time = time.time() + timeout
    while time.time() < end_time:
        if condition():
            return True
        time.sleep(0.1)
    return False

def get_updated_devices(connection):
    pass

# Main function

def main():
    tracking_listener = TrackingEventListener()
    device_listener = MultiDeviceListener(None)

    connection = Connection(multi_device_aware=True)
    connection.add_listener(tracking_listener)
    connection.add_listener(device_listener)

    with connection.open():
        wait_until(lambda: device_listener.n_events > 1)

        current_device_events = device_listener.n_events
        get_updated_devices(connection)

        while True:
            if device_listener.n_events != current_device_events:
                print("device_listener got a new device event")
                current_device_events = device_listener.n_events
                get_updated_devices(connection)

            time.sleep(0.5)
