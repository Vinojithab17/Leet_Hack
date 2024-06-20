import csv
import numpy as np

class Canvas:
    def __init__(self):
        self.name = "MockCanvas"
        self.screen_size = (640, 480)
        self.clearCanvas = False
        self.output_image = np.zeros((self.screen_size[0], self.screen_size[1], 3), np.uint8)

    def set_tracking_mode(self, mode):
        pass

class Connection:
    def __init__(self):
        pass

    def open(self):
        return self

    def set_tracking_mode(self, mode):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def create_csv_file(csv_file_path, header):
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

def update_canvas(canvas, csv_file_path, header):
    imgCanvas = np.zeros((canvas.screen_size[0], canvas.screen_size[1], 3), np.uint8)
    if canvas.clearCanvas:
        imgCanvas = np.zeros((canvas.screen_size[0], canvas.screen_size[1], 3), np.uint8)
        canvas.clearCanvas = False
        create_csv_file(csv_file_path, header)
    return imgCanvas

def main():
    canvas = Canvas()
    print(canvas.name)
    running = True
    header = ['frame_id', 'index_x_coor', 'index_y_coor', 'index_z_coor',
              'palm_x_coor', 'palm_y_coor', 'palm_z_coor', 'index_x_velocity',
              'index_y_velocity', 'index_z_velocity', 'palm_velocity_x',
              'palm_velocity_y', 'palm_velocity_z', 'confidence',
              'hand_grab_angle', 'hand_grab_strength', 'armPosition_x',
              'armPosition_y', 'armPosition_z', 'tip_rotation_x',
              'tip_rotation_y', 'tip_rotation_z', 'tip_rotation_w', 'target']
   
    csv_file_path = '{FileName}.csv'.format(FileName=input("Enter File Count : "))
    create_csv_file(csv_file_path, header)

    connection = Connection()
    with connection.open():
        connection.set_tracking_mode("Desktop")
        canvas.set_tracking_mode("Desktop")

        imgCanvas = np.zeros((canvas.screen_size[0], canvas.screen_size[1], 3), np.uint8)
        x1, y1 = 0, 0
        Actual_x, Actual_y, Actual_z = 0, 0, 0
        
        while running:
            frame = canvas.output_image
            imgCanvas = update_canvas(canvas, csv_file_path, header)
            # Simulate condition to stop running to avoid infinite loop during testing
            running = False

if __name__ == "__main__":
    main()
