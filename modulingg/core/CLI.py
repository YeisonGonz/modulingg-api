import cmd
import os
import subprocess

from modulingg.controllers.logger import log_message
from modulingg.core.utils import only_manifest, only_modules, print_manifest

FASTAPI_COMMAND_DEV = ["fastapi", "dev", "modulingg/fastapi_core.py"]
FASTAPI_COMMAND_PR = ["fastapi", "run", "modulingg/fastapi_core.py"]

fastapi_status = 'FASTAPI_STATUS'

class CLI(cmd.Cmd):
    intro = "Welcome to Modulingg 📦. Type 'help' or '?' to see the commands.\n"
    prompt = "📦 > "

    def do_run(self, arg):
        if arg == "dev":
            try:
                subprocess.run(FASTAPI_COMMAND_DEV)
            except KeyboardInterrupt:
                log_message('INFO', '    Modulingg shutdown.')
                
        if arg == "pr":
            try:
                subprocess.run(FASTAPI_COMMAND_PR)
            except KeyboardInterrupt:
                log_message('INFO', '    Modulingg shutdown.')
                
                
    def do_info(self, arg):
        all_modules = only_modules()
        if arg == "":
            print("You must enter the name of a module.")
            return

        try:
            index = all_modules.index(arg) 
            manifest = only_manifest()[index] 
            print_manifest(manifest)
        except ValueError:
            print(f"The module '{arg}' does not exist in the list.")


    def do_runmodule(self, arg):
        all_modules = only_modules()
        try:
            if arg in all_modules:               
                fastapi_status = "mono_module" 
                os.environ["FASTAPI_STATUS"] = fastapi_status
                os.environ["FASTAPI_MODULE"] = arg
                
                subprocess.run(FASTAPI_COMMAND_DEV)
                
           
        except ValueError:
            print(f"The module '{arg}' does not exist in the list.")
        


    def do_exit(self, arg):
        print("Goodbye...")
        return True


    # Manejo de error de comando no encontrado
    def default(self, line):
        print(f"Unknow command: {line}")
        
if __name__ == '__main__':
    try:
        CLI().cmdloop()
    except KeyboardInterrupt:
        print("Goodbye...")
