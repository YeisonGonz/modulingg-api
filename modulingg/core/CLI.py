import cmd
import os

from modulingg.controllers.ModuleManager import ModuleManager
from modulingg.controllers.config import CONFIGURATION, Config, DynamicConfig
from modulingg.controllers.logger import log_message
from modulingg.core.Launcher import Launcher
from modulingg.core.help import Help
from modulingg.core.utils import only_manifest, only_modules, print_manifest
from modulingg.decorators.commandManager import commandManager

fastapi_status = 'FASTAPI_STATUS'
launcher = Launcher()

class CLI(cmd.Cmd):
    intro = "Welcome to Modulingg 📦. Type 'help' or '?' to see the commands.\n"
    prompt = "📦 > "
    
    @commandManager
    def do_run(self, arg):
        os.environ["FASTAPI_STATUS"] = "multi_module"
        if arg == "dev":
            try:
                launcher.launchApp("development")
            except KeyboardInterrupt:
                log_message('INFO', '    Modulingg shutdown.')
                
        if arg == "pr":
            try:
                launcher.launchApp()
            except KeyboardInterrupt:
                log_message('INFO', '    Modulingg shutdown.')
    
    @commandManager                   
    def do_clear(self,arg):
        if os.name == 'nt':
            os.system('cls')  # For Windows
        else:
            os.system('clear')  # For macOS/Linux
    
    @commandManager     
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

    @commandManager
    def do_runmodule(self, arg):
        all_modules = only_modules()
        try:
            if arg in all_modules:               
                fastapi_status = "mono_module" 
                os.environ["FASTAPI_STATUS"] = fastapi_status
                os.environ["FASTAPI_MODULE"] = arg
                
                launcher.launchApp("development")
            else:
                print(f"The module '{arg}' does not exist in the list.")
        except ValueError:
            print(f"The module '{arg}' does not exist in the list.")
        except KeyboardInterrupt:
            log_message('INFO', '    Modulingg shutdown.')

    @commandManager
    def do_help(self, arg):
        Help(arg)

    
    # Launch FASTAPI server and return all the endpoints of the module selected
    @commandManager
    def do_endmodule(self,arg):
        all_modules = only_modules()
        try:
            if arg in all_modules:               
                fastapi_status = "inspector" 
                os.environ["FASTAPI_STATUS"] = fastapi_status
                os.environ["FASTAPI_MODULE"] = arg
                
                launcher.launchApp("inspector")
            else:
                print(f"The module '{arg}' does not exist in the list.")
        except ValueError:
            print(f"The module '{arg}' does not exist in the list.")
        except KeyboardInterrupt:
            log_message('INFO', '    Modulingg shutdown.')

    @commandManager
    def do_config(self, arg):
        args = arg.split()
        config_params = CONFIGURATION.keys()

        try:
            if len(args) == 0:
                print(f"Usage: config [key] --set/--get [value]")
                return

            if args[0] not in config_params:
                print(f"Invalid key. Available keys: {', '.join(config_params)}")
                return
                
            if len(args) == 3 and args[1] == "--set":
                param = args[0]
                value = args[2]
                if Config.write_config(param,value):
                    print(f"The value '{value}' has been saved for the key '{param}'.")
                else:
                    print(f"An error occurred while saving the value.")
                    
            if len(args) == 2 and args[1] == "--get":
                print(CONFIGURATION[args[0]])
        except Exception as e:
            print(f"An error occurred")
        except FileNotFoundError:
            print("The configuration file could not be found.")
    
    @commandManager
    def do_module(self,arg):
        try:
            module_manager = ModuleManager()
            args = arg.split()
            if args[0] == 'make':
                module_manager.makeDefaultModules()
            if args[0] == 'list':
                module_manager.moduleList()
            if args[0] == 'copy' and args[1]:
                module_manager.copyModule(args[1])
            if args[0] == 'remove' and args[1]:
                module_manager.deleteModule(args[1])
        except Exception as e:
            print(e)
            
            
    def do_EOF(self,arg):
        print("Goodbye...")
        return True

    @commandManager
    def do_exit(self,arg):
        print("Goodbye...")
        return True


    def default(self, line):
        print(f"Unknow command: {line}")
        
if __name__ == '__main__':
    try:
        CLI().cmdloop()
    except KeyboardInterrupt:
        print("Goodbye...")
