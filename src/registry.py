from typing import TypeVar, Generic
Content = TypeVar("Content")

class Identifier:
    def __init__(self,namespace: str, path: str):
        self.namespace = namespace
        self.path = path
    
    def equals(self, other):
        if not isinstance(other,Identifier):
            return False
        
        return self.namespace == other.namespace and self.path == other.path
    
    def tostr(self):
        return "%s:%s".format(self.namespace,self.path)

class Registry(Generic[Content]):
    def __init__(self):
        self._store: dict[Identifier,Content] = {}
    
    def register(self,id: Identifier, content: Content):
        if id in self._store.keys():
            return ValueError("Registry entries are immutable! Duplicate Identifier: "+id)
        
        self._store.setdefault(id,content)
        if hasattr(content,"onRegister"):
            content.onRegister(id,self)
        
        return content

#Helper to make Identifiers less of a pain
def id(string: str):
    split = string.split(":")
    if (len(split) == 2):
        return Identifier(split[0],split[1])

    return ValueError("Invalid input string, expected 'namespace:path' got: '%s'".format(string))
