from pyray import *
from src.shared import EventManager
from src.worlds import WorldData

class Enemy:
    def __init__(self, border_idx: int, world: WorldData, velocity: float, event_manager: EventManager):
        self.event_manager = event_manager
        self.border_idx = border_idx
        self.world = world
        self.velocity = velocity
        self.event_manager.subscribe(EventManager.Topics.BLASTER_BULLET_UPDATE, self.blaster_bullet_update)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, border: {self.border_idx}"
    
    def blaster_bullet_update(self, data: dict):
        pass
    
    def update_frame(self):
        pass

    def draw_frame(self):
        pass