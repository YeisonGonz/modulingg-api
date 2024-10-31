import zipfile
import shutil

from modulingg.controllers.autoload import Autoloader
from modulingg.controllers.config import CONFIGURATION
from modulingg.schemas.templates import MODULE_LIST_TEMPLATE

class ModuleManager():
    DEFAULT_MODULE_ZIPFILE = 'modulingg/resources/df-md.zip'  
    
    def __init__(self):
        self.loader = Autoloader()
        self.modules_list = self.loader.search_modules()
        pass
    
    # Make a new module, unzip a previously defined module.
    @staticmethod
    def makeDefaultModules():
        try:
            with zipfile.ZipFile(ModuleManager.DEFAULT_MODULE_ZIPFILE, 'r') as zip_ref:
                zip_ref.extractall(CONFIGURATION['modules_folder_name'])
            print(f"Default modules have been successfully created in '{CONFIGURATION['modules_folder_name']}'.")
        except FileNotFoundError:
            print(f"The module zip file '{ModuleManager.DEFAULT_MODULE_ZIPFILE}' does not exist.")
        except PermissionError as e:
            print(f"Permission denied to open the '{CONFIGURATION['modules_folder_name']}' folder. ({str(e)})")
    
    
    def moduleList(self):
        for module in self.modules_list:
            print(f"\n\t{MODULE_LIST_TEMPLATE.format(module[0], module[1].name,module[1].short_name,module[1].description,module[1].author,module[1].version)}")
    
    
    # Copy a module folder
    def copyModule(self, moduleToCopy):
        try:
            module_copy_path = f"{CONFIGURATION['modules_folder_name']}/{moduleToCopy}"
            shutil.copytree(module_copy_path,module_copy_path+'_copy')
            print(f"Module '{moduleToCopy}' has been successfully copied.")
        except OSError:
            print(f"This isnt a valid module.")
        except Exception as e:
            print(e)
            
    # Delete a module folder
    def deleteModule(self, moduleToDelete):
        try:
            module_delete_path = f"{CONFIGURATION['modules_folder_name']}/{moduleToDelete}"
            shutil.rmtree(module_delete_path)
            print(f"Module '{moduleToDelete}' has been successfully delete.")
        except FileNotFoundError:
            print(f"This isnt a valid module to delete.")
        except Exception as e:
            print(e)
