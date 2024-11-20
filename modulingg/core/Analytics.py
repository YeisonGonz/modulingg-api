import io
import json
import matplotlib.pyplot as plt
import pandas as pd

from modulingg.core.Metrics import MetricManager 

class Analytics:
    
    def __init__(self) -> None:
        self.metrics_object = MetricManager()

    def load_analytics(self):
        all_metric_names = self.metrics_object._get_all_metrics()
        dataframes = []
        
        for metric_name in all_metric_names:
            metric_file_name = f"{self.metrics_object.metric_data_folder}/{metric_name}"
            output_file_name = metric_file_name.replace(".json", ".jsonl")  

            self.metrics_object.convert_to_jsonl(metric_file_name, output_file_name)

            try:
                df = pd.read_json(output_file_name, lines=True)
                dataframes.append(df)
            except ValueError as e:
                print(f"Failed to load metrics data from {output_file_name}: {e}")

        if dataframes:
            combined_df = pd.concat(dataframes, ignore_index=True)
            return combined_df
        else:
            print("No data was loaded. Returning an empty DataFrame.")
            return pd.DataFrame()
            
            
    def _make_graph(self,x_values, y_values):
        plt.figure(figsize=(15,5))
        plt.bar(x=x_values,height=y_values, width=0.4,color='red',edgecolor='k',alpha=0.6)
        plt.xticks(fontsize=12,rotation=45)
        plt.yticks(fontsize=10)
        img_stream = io.BytesIO()
        plt.tight_layout()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)
        plt.close()
        
        return img_stream
            
    def make_graph_analytics_endpoints(self, df_analytics):
        df_analytics['url'] = df_analytics['url'].str.replace('http://127.0.0.1:8100', '', regex=False)
        df_grouped = df_analytics.groupby(['url']).size().reset_index(name='count')
        
        return self._make_graph(df_grouped['url'].values, df_grouped['count'].values)

    
    def make_graph_analytics_by_ip(self, df_analytics):
        df_grouped = df_analytics.groupby(['ip']).size().reset_index(name='count')
        
        return self._make_graph(df_grouped['ip'].values, df_grouped['count'].values)

    
    
    def make_graph_analytics_by_lang(self, df_analytics):
        df_grouped = df_analytics.copy()
        df_grouped['accept_language'] = df_grouped['headers'].apply(
            lambda x: x.get('accept-language', '').split(',')[0] if isinstance(x, dict) and 'accept-language' in x else None
        )

        lang_counts = df_grouped['accept_language'].value_counts()
        
        return self._make_graph(lang_counts.index, lang_counts.values)
