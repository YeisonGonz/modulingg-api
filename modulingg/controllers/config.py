import json
from typing import Optional

from pydantic import BaseModel, Field

CONFIG_FILE = 'modulingg/config/config.json'
COMMANDS_DIRECTORY_FILE = 'modulingg/config/commands.json'


class Config:
    def read_config(self):
        try:
            with open(CONFIG_FILE, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Error to find the configuration file. The default location is 'modulingg/config/config.json'.")
            exit(-1)
            
    
    @staticmethod
    def write_config(param, value):
        try:
            with open(CONFIG_FILE, 'r') as file:
                data = json.load(file)
            if param in data:
                data[param] = value
            else:
                return False
            
            with open(CONFIG_FILE, 'w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("Error to find the configuration file.")
        except json.JSONDecodeError:
            print("Error to read the JSON file.")


class CommandsDictionary:
    def read_config(self):
        with open(COMMANDS_DIRECTORY_FILE, 'r') as file:
            data = json.load(file)
        return data

CONFIGURATION = Config().read_config()


class Manifest(BaseModel):
    name: str
    short_name: Optional[str] = None
    description: Optional[str] = None
    author: str
    version: str 

    @classmethod
    def read_config(cls, manifest_file: str):
        with open(manifest_file, 'r') as file:
            data = json.load(file)
        return cls(**data)
