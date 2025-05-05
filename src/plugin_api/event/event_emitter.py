from uuid import uuid4

class EventEmitter:
    def __init__(self,*events: str):
        print
        self._evtHandlers = {}
        for evt in events:
            self._evtHandlers.setdefault(evt,{})
    
    def on(self,evt,handler):
        if not evt in self._evtHandlers.keys():
            raise ValueError(f"Event {evt} doesn't exist on Registry {self._name}!")

        uuid = uuid4()
        self._evtHandlers[evt].set_default(uuid,handler)
        return uuid
    
    def off(self,evt,uuid):
        if not evt in self._evtHandlers.keys():
            raise ValueError(f"Event {evt} doesn't exist on Registry {self.name}!")
        if not uuid in self._evtHandlers[evt].keys():
            raise ValueError(f"Handler with UUID {uuid} not found for {evt} on Registry {self.name}!")
        
        return self._evtHandlers[evt].pop(uuid)

    def _emit(self,evt,*args):
        if evt not in self._evtHandlers.keys():
            raise ValueError(f"Event {evt} doesn't exist on Registry {self.name}!")
        
        cancel = False
        for handler in self._evtHandlers[evt].keys():
            retval = self._evtHandlers[evt][handler](self,cancel,*args)
            if retval == False:
                cancel = True

        return cancel