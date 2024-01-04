from .objects import Event
from ..vk import Vk


class EventManager:
    def __init__(self) -> None:
        self.events = {}

    def register_event(self, name: str) -> None:
        def wrapper(func):
            self.events[name] = func
        return wrapper
    
    def use_event(self, name: str, event: Event, vk: Vk):
        if name in self.events:
            return self.events[name](event, vk)
        return
