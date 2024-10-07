import json

from pydantic import BaseModel

CONFIG_FILE = './config/config.json'


class Config:
    def read_config(self):
        with open(CONFIG_FILE, 'r') as file:
            data = json.load(file)
        return data

CONFIGURATION = Config().read_config()