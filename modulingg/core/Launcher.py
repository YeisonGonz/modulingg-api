import subprocess
import uvicorn

from modulingg.controllers.config import CONFIGURATION

class Launcher:

    def __init__(self):
        self.FASTAPI_MODULE_NAME = "modulingg.fastapi_core:app"
        self.FASTAPI_HOST = CONFIGURATION['launcher_fastapi_host']
        self.FASTAPI_LAUNCHER_PORT = CONFIGURATION['launcher_fastapi_port']
        self.FASTAPI_COMMAND_DEV = ["fastapi", "dev", "modulingg/fastapi_core.py", "--port", str(self.FASTAPI_LAUNCHER_PORT)]
        self.FASTAPI_COMMAND_DEV_NOLOG = ["uvicorn", self.FASTAPI_MODULE_NAME, "--log-level", "critical","--port",str(self.FASTAPI_LAUNCHER_PORT)]
        pass
    
    def launchApp(self, mode="production"):
        if mode == "development":
            subprocess.run(self.FASTAPI_COMMAND_DEV)
        elif mode == "production":
            uvicorn.run(self.FASTAPI_MODULE_NAME, port=8000, host=self.FASTAPI_HOST)
        elif mode == "inspector":
            subprocess.run(self.FASTAPI_COMMAND_DEV_NOLOG)
    
    
def run():
    launcher = Launcher()
    launcher.launchApp('development')
            
    