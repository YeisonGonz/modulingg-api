import io
import json
import matplotlib.pyplot as plt
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
            
    def make_graph_analytics_endpoints(self, df_analytics):
        df_analytics['url'] = df_analytics['url'].str.replace('http://127.0.0.1:8100', '', regex=False)
        df_grouped = df_analytics.groupby(['url']).size().reset_index(name='count')
        plt.figure(figsize=(15,5))
        plt.bar(x=df_grouped['url'].values,height=df_grouped['count'].values, width=0.4,color='blue',edgecolor='k',alpha=0.6)
        plt.xticks(fontsize=12,rotation=45)
        plt.yticks(fontsize=10)
        img_stream = io.BytesIO()
        plt.tight_layout()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        plt.close()
        
        return img_stream
    
    def make_graph_analytics_by_ip(self, df_analytics):
        df_analytics['url'] = df_analytics['ip']
        df_grouped = df_analytics.groupby(['ip']).size().reset_index(name='count')
        
        plt.figure(figsize=(15,5))
        plt.bar(x=df_grouped['ip'].values,height=df_grouped['count'].values, width=0.4,color='blue',edgecolor='k',alpha=0.6)
        plt.xticks(fontsize=12,rotation=45)
        plt.yticks(fontsize=10)
        img_stream = io.BytesIO()
        plt.tight_layout()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        plt.close()
        
        return img_stream