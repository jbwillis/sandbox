from .module_core import ModuleCore

class ModuleExtended(ModuleCore):
    def __init__(self):
        print("Module Extended Init")
        super().__init__()
