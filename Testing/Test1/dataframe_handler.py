import pandas as pd
from datetime import datetime

class DataFrameHandler:
    def __init__(self, new_df, frame_id_list, csv_file_path):
        self.new_df = new_df
        self.frame_id_list = frame_id_list
        self.csv_file_path = csv_file_path

    def save_dataframe_to_csv(self):
        # Update coordinates target
        for fid in self.frame_id_list:
            try:
                self.new_df.at[self.new_df.loc[self.new_df['frame_id'] == fid].index[0], 'target'] = 0
            except IndexError:
                pass
        
        now = datetime.now()
        date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
        csv_file_name = f'Signatures/updated_{self.csv_file_path}.csv'
        self.new_df.to_csv(csv_file_name, index=False)
