from src.plugin_api.registry.identifier import Identifier

class Plugin:
    def __init__(self,pluginhelper):
        self.helper = pluginhelper

    def pre(self): # Is run before registry initialization
        pass
    
    def registry(self): # Is run as part of registry initialization. Define moves & battlers, etc. here!
        pass
        
    def ready(self): # Is run after the game is ready to go
        pass

    def ipc_received(self,other_name,message):
        pass