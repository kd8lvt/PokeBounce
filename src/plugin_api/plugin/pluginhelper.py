from src.plugin_api.registry.registry import Registry
from src.plugin_api.plugin.plugin import Plugin
from src.plugin_api.registry.identifier import Identifier
from src.plugin_api.registry.registries import registries

class PluginHelper:
    def __init__(self,plugin: Plugin):
        self._plugin = plugin(self)
        self._registries = registries
        self.get_registry(Identifier("vanilla","plugins")).register(self._plugin.id,self._plugin)

    
    def get_registry(self,iden: Identifier):
        return self._registries.get(iden)

    def send_ipc(self,other_id: Identifier, message): # Send something to another plugin. They might not do anything with it, but it's an option.
        self.get_registry(Identifier("main","plugins")).get(other_id).received_ipc(self._plugin.id,message)
    
    def id(self,path: str): # Returns an identifier with your namespace
        return Identifier(self._plugin.namespace,path)