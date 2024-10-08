import cmd
import subprocess

from modulingg.controllers.logger import log_message
from modulingg.core.utils import only_manifest, only_modules, print_manifest

class CLI(cmd.Cmd):
    intro = "Welcome to Modulingg 📦. Type 'help' or '?' to see the commands.\n"
    prompt = "📦 > "

    def do_run(self, arg):
        command = ["fastapi", "dev", "modulingg/fastapi_core.py"]
        command_prod = ["fastapi", "run", "modulingg/fastapi_core.py"]
        
        if arg == "dev":
            try:
                subprocess.run(command)
            except KeyboardInterrupt:
                log_message('INFO', '    Modulingg shutdown.')
                
        if arg == "pr":
            try:
                subprocess.run(command_prod)
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


    def do_exit(self, arg):
        print("Goodbye...")
        return True


    # Manejo de error de comando no encontrado
    def default(self, line):
        print(f"Unknow command: {line}")
        
if __name__ == '__main__':
    CLI().cmdloop()
