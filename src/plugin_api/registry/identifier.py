class Identifier:
    def __init__(self, namespace: str, path: str):
        self.namespace = namespace
        self.path = path
    @staticmethod
    def from_string(string: str):
        split = string.split(":")
        if (len(split) == 2):
            return Identifier(*split)
        
        raise ValueError(f"Expected 'namespace:path', got '{string}'")
    
    def equals(self, other):
        if not isinstance(other,Identifier):
            raise TypeError(f"Expected {Identifier}, got {type(other)}")
        return self is other or (self.namespace == other.namespace and self.path == other.path)
    
    def tostring(self):
        return f"{self.namespace}:{self.path}"