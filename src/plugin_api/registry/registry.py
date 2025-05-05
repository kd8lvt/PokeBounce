from typing import TypeVar, Generic
from src.plugin_api.registry.identifier import Identifier
from src.plugin_api.event.event_emitter import EventEmitter

Content = Generic[TypeVar('Content')]

class Registry(EventEmitter,Content):
    def __init__(self,name):
        super().__init__("before_register","after_register")
        self._name = name
        self._content: dict[Identifier,Content] = {}
    
    def register(self, id: Identifier, thing: Content):
        for key in self._content.keys():
            if id.tostring() == key:
                raise ValueError(f"Identifier {id} already used by another {type(thing)}!")
        
        if self._emit("before_register",id,thing): #if the before_register event is canceled
            return None #don't do anything else, and return None as a warning
        
        self._content.setdefault(id.tostring(),thing)
        self._emit("after_register",id)
        return thing

    def keys(self):
        return self._content.keys()

    def get(self,id: Identifier):
        return self._content[id.tostring()]

    def foreach(self,callback):
        for key in self._content.keys():
            callback(self._content[key])