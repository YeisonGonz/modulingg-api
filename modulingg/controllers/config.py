import json
import copy

import os
from typing import Optional
from pydantic import BaseModel, Field

# These are all default values, they can be permanently changed via the Config interface,
# the safest way to modify the configuration is at run time, via the ConfigInterface interface and 
# DynamicConfig it is made to modify and obtain configuration internally.

CONFIG_FILE = 'modulingg/config/config.json'
COMMANDS_DIRECTORY_FILE = 'modulingg/config/commands.json'
COMMANDS_DIRECTORY_HELP_FILE = 'modulingg/config/commandhelp.json'


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


# This interface is used inn mode Library, no in internal settings
class ConfigInterface:
    @staticmethod
    def set(param, value):
        tempConfig = DynamicConfig()
        tempConfig.set(param, value)

class DynamicConfig:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DynamicConfig, cls).__new__(cls)
            cls._instance.all_config = copy.copy(CONFIGURATION)
            
            cls._instance.all_config["launcher_fastapi_port"] = os.getenv('API_PORT', CONFIGURATION["launcher_fastapi_port"])
            cls._instance.all_config["modulingg_prefix"] = os.getenv('API_PREFIX', CONFIGURATION["modulingg_prefix"])
        return cls._instance

    def get(self, key):
        return self.all_config.get(key)

    def set(self, key, value):
        self.all_config[key] = value

class CommandsDictionary:
    def read_config(self):
        with open(COMMANDS_DIRECTORY_FILE, 'r') as file:
            data = json.load(file)
        return data
    
class CommandsDictionaryHelp:
    def read_config():
        with open(COMMANDS_DIRECTORY_HELP_FILE, 'r') as file:
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
