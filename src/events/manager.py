from .objects import Event 


class EventManager:
    def __init__(self) -> None:
        self.events = {}

    def register_event(self, name: str) -> None:
        def wrapper(func):
            self.events[name] = func
        return wrapper
    
    def use_event(self, name: str, event: Event):
        if name in self.events:
            return self.events[name]()
        return
