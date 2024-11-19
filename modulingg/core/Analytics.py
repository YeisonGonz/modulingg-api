import json
import pandas as pd

from modulingg.core.Metrics import MetricManager 

class Analytics:
    
    def __init__(self) -> None:
        self.metrics_object = MetricManager()

    def load_analytics(self):
        last_metric_name = self.metrics_object._get_last_metricname()
        metric_file_name = f"{self.metrics_object.metric_data_folder}/{last_metric_name}"
        output_file_name = metric_file_name.replace(".json", ".jsonl") # Converted file lives in execution time. 

        self.metrics_object.convert_to_jsonl(metric_file_name, output_file_name)

        try:
            df = pd.read_json(output_file_name, lines=True)
            return df
        except ValueError as e:
            print(f"Failed to load metrics data: {e}")