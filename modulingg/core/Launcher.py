import subprocess
import uvicorn
import os

from controllers.config import DynamicConfig

class Launcher:

    def __init__(self):
        self.config = DynamicConfig()
        self.FASTAPI_MODULE_NAME = "modulingg.fastapi_core:app"
        self.FASTAPI_HOST = self.config.get('launcher_fastapi_host')
        self.FASTAPI_LAUNCHER_PORT = self.config.get('launcher_fastapi_port')
        self.FASTAPI_COMMAND_DEV = ["fastapi", "dev", "modulingg/fastapi_core.py", "--port", str(self.FASTAPI_LAUNCHER_PORT), "--host", '0.0.0.0']
        self.FASTAPI_COMMAND_PR = ["fastapi", "run", "modulingg/fastapi_core.py", "--port", str(self.FASTAPI_LAUNCHER_PORT), "--host", '0.0.0.0']
        self.FASTAPI_COMMAND_DEV_NOLOG = ["uvicorn", self.FASTAPI_MODULE_NAME, "--log-level", "critical","--port",str(self.FASTAPI_LAUNCHER_PORT)]
        pass
    
    def launchApp(self, mode="production"):

        print('Api mode', os.getenv('API_MODE'))
        if mode == "development":
            subprocess.run(self.FASTAPI_COMMAND_DEV)
        elif mode == "production":
            subprocess.run(self.FASTAPI_COMMAND_PR)
        elif mode == "inspector":
            subprocess.run(self.FASTAPI_COMMAND_DEV_NOLOG)
    

class LauncherInterface:
    @staticmethod
    def dev():
        temp_launcher = Launcher()
        temp_launcher.launchApp('development')

    
    @staticmethod
    def pr():
        temp_launcher = Launcher()
        temp_launcher.launchApp('development')

    @staticmethod
    def run():
        temp_launcher = Launcher()
        temp_launcher.launchApp(os.getenv('API_MODE', 'production'))    