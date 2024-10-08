from pydantic import BaseModel
from typing import List, Union

class HostResponse(BaseModel):
    message: str = "Welcome to Modulingg"
    version: str = "1.0.1"    


class ModulesListResponse(BaseModel):
    modules: Union[List[str], str]
    
    def __init__(self, **data):
        super().__init__(**data)
        
        if not self.modules:
            self.modules = "No se ha cargado ningún módulo."
            
            
class Module(BaseModel):
    name: str
    endpoints: List[str]