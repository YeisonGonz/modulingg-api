

import os


class MetricManager:

    # Return number with all data values 
    def __str__(self) -> str:
        pass

    def __init__(self) -> None:
        self.metric_data_folder = './modulingg/metrics'
        self.metric_data_basefilename = 'metric_'

    def _get_last_metricname(self):
        try:
            all_files_name = os.listdir(self.metric_data_folder)
            last_metric_register = sorted(all_files_name)[::-1][0]
            return last_metric_register
        except FileNotFoundError:
            return None
        except PermissionError:
            print('MetricManager dont have permission.')
            return None


    def _calculate_hash_name(self, last_metric_name):
        try:
            last_hash = int(last_metric_name.split(self.metric_data_basefilename)[1])

            # Calculate all 0 to fill the new hash number
            if len(str(last_hash)) < len(last_metric_name.split(self.metric_data_basefilename)[1]):
                last_hash = ('0'*(len(last_metric_name.split(self.metric_data_basefilename)[1])-len(str(last_hash)))) + str(last_hash+1)

            return self.metric_data_basefilename+last_hash
        except PermissionError:
            print('MetricManager dont have permission.')
            return None

    # def _make_new_metric(self):

    # def append_metric_value(self):

    