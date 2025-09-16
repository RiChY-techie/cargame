# backend.py

from ursina import *
import random

class CarGameLogic(Entity):
    def __init__(self):
        super().__init__()
        self.car = None
        self.road = None
        self.mountains = []
        self.is_paused = False

    def setup_game(self):
        self.create_road()
        self.create_car()
        self.create_mountains()

    def create_road(self):
        self.road = Entity(model='cube', color=color.gray, scale=(10, 1, 100), position=(0, 0, 0))

    def create_car(self):
        self.car = Entity(model='cube', color=color.red, scale=(1, 0.5, 2), position=(0, 0.5, -5))
        self.car.rotation_y = 90  # Facing forward

    def create_mountains(self):
        self.mountains = []
        for _ in range(5):
            mountain = Entity(model='cube',
                              color=color.brown,
                              scale=(random.uniform(3, 5), random.uniform(3, 5), random.uniform(3, 5)),
                              position=(random.uniform(-20, 20), random.uniform(1, 5), random.uniform(-50, 0)))
            self.mountains.append(mountain)

    def drift(self):
        self.car.rotation_y += 15
        invoke(self.reset_drift, delay=0.5)
        
    def reset_drift(self):
        self.car.rotation_y -= 15

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Game Paused")
        else:
            print("Game Resumed")
