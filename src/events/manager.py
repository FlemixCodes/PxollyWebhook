from .objects import Event
from ..vk import Vk


class EventManager:
    def __init__(self) -> None:
        self.events = {}

    def register_event(self, name: str) -> None:
        def wrapper(func):
            self.events[name] = func
        return wrapper
    
    def use_event(self, event: Event, vk: Vk):
        if event.type in self.events:
            return self.events[event.type](event, vk)
        return
