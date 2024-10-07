import importlib
import os
from typing import List

from pydantic import BaseModel

from controllers.config import CONFIGURATION, Config
from controllers.logger import log_message
from schemas.basic_response import Module

MODULES_FOLDER = CONFIGURATION['modules_folder_name']
INIT_FILE = CONFIGURATION['module_launcher_name']

class ModuleVerifier(BaseModel):
    modules: List[Module] = [] 
    
    def append(self, module: Module):
        module_name = module.name
        all_endpoints = {endpoint for mod in self.modules for endpoint in mod.endpoints}
        
        duplicate_endpoints = [ep for ep in module.endpoints if ep in all_endpoints]
        
        if duplicate_endpoints:
            log_message('WARNING', f'The following endpoints already exist: {duplicate_endpoints} in ({module_name})')
        
        self.modules.append(module)

# Busca todos los modulos disponibles
def search_modules():
    founded_modules = []
    for foldername in os.listdir(MODULES_FOLDER):
        folder_path = os.path.join(MODULES_FOLDER, foldername)
        
        try:
            if os.path.isdir(folder_path):
                main_file = os.path.join(folder_path, f'{INIT_FILE}.py')
                
                if os.path.exists(main_file):
                    module_name = f'{MODULES_FOLDER}.{foldername}.{INIT_FILE}'
                    founded_modules.append(module_name)
        except Exception as e:
            log_message('ERROR', f"Error searching module {foldername} ❌ ({str(e)})")
    
    return founded_modules
 

# Lee la lista de modulos a incluir en el Router
def include_module_list(moduleList: List[str], fastApiApp) -> List[str]:
    modules_loaded = []
    moduleVerifier = ModuleVerifier()

    for module_name in moduleList:
        try:
            module = importlib.import_module(module_name)
            fastApiApp.include_router(module.router)        
            completeModule = makeModule(module.router.routes, module_name)
            moduleVerifier.append(completeModule)
            modules_loaded.append(module_name)

            log_message('INFO', f'  -   Loaded {module_name} 📦 ({module_name})')
        except Exception as e:
            log_message('ERROR', f"Error loading module {module_name} ❌ ({str(e)})")
    
    return modules_loaded

def autoload_modules(fastApiApp):  
    loaded_modules = []
    
    log_message('INFO', f'Starting Modulingg 📦')
    log_message('INFO', f'Searching for modules in {MODULES_FOLDER}...')
    module_whitelist_status = CONFIGURATION['module_whitelist']
    
    all_modules = search_modules()
    
    if module_whitelist_status:
        enabled_modules = CONFIGURATION['enabled_modules_whitelist']
        enabled_modules_in_all = [module for module in all_modules if module in enabled_modules]
        loaded_modules = include_module_list(enabled_modules_in_all,fastApiApp)
    else:
        loaded_modules = include_module_list(all_modules,fastApiApp)
    
    log_message('INFO', f'Modules loaded {len(loaded_modules)} successfully ')
    return loaded_modules
                
                
def makeModule(moduleRouteApi, moduleName) -> Module:
    endpoints = []
    for moduleRoute in moduleRouteApi:
        endpoints.append(moduleRoute.path)
        
    return Module(name=moduleName, endpoints=endpoints)