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
            if all_files_name == []:
                return self.metric_data_basefilename+'0000'
            
            last_metric_register = sorted(all_files_name)[::-1][0]
            return last_metric_register
        except FileNotFoundError:
            return None
        except PermissionError as e:
            print('MetricManager dont have permission.',e)
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
        
    def _make_new_metric(self, metric_data):
        try:
            last_metric_name = self._get_last_metricname()
            new_metric_name = self._calculate_hash_name(last_metric_name)
            
            directory = self.metric_data_folder
            if not os.path.exists(directory):
                os.makedirs(directory)
                
            if self._get_entry_metric_file(last_metric_name) >= 100:
                with open(f"{directory}/{new_metric_name}", "w") as file:
                    file.write(str(metric_data) + '\n')
                return True
            
            with open(f"{directory}/{last_metric_name}", "a") as file:
                file.write(str(metric_data) + '\n')
            return True
            
        except PermissionError as e:
            print('MetricManager dont have permission.', e)
            return False
        except FileNotFoundError as e:
            print('Create a metrics folder', e)
            return False
       

    def _get_entry_metric_file(self, metric_file):
        try:
            with open(f"{self.metric_data_folder}/{metric_file}", "r") as file:
                metric_lines = sum(1 for line in file)
            return metric_lines
        except PermissionError as e:
            print('MetricManager dont have permission.',e)


    def append_metric_value(self, metric_data):
        return self._make_new_metric(metric_data)
        

    