from typing import Dict
from ..entities.ball import Ball
from pygame.math import Vector2


class EntityManager:

    def __init__(self) -> None:
        
        self.ball_dict: Dict[str, Ball] = {}

    def apply_force(self, force: int) -> None:
        for entity in self.ball_dict.values():
            entity.apply_force(Vector2(force, -abs(force)))

    def update_entities(self, delta_time:float) -> None:
        for entity in self.ball_dict.values():
            entity._update(delta_time)
    
    def add(self, ball: Ball) -> None:
        self.ball_dict[ball.id] = ball

    def delete_all(self) -> None:
        self.ball_dict = {}

    def draw(self, screen) -> None:
        for entity in self.ball_dict.values():
            entity.draw(screen)    
