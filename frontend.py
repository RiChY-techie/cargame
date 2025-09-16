# frontend.py

from ursina import *
from backend import CarGameLogic

class CarGameFrontend(Entity):
    def __init__(self):
        super().__init__()
        self.logic = CarGameLogic()
        self.logic.setup_game()
        camera.position = (0, 20, -35)
        camera.look_at(self.logic.car)

        # Controls
        self.speed = 0
        self.turn_speed = 1.5

    def input(self, key):
        if key == 'space':
            self.logic.drift()
        if key == 'escape':
            self.logic.toggle_pause()

    def update(self):
        if self.logic.is_paused: return

        # Car movement: Forward/back and left/right rotation
        if held_keys['w']:
            self.logic.car.position += self.logic.car.forward * 0.2
        if held_keys['s']:
            self.logic.car.position += self.logic.car.back * 0.1
        if held_keys['a']:
            self.logic.car.rotation_y += self.turn_speed
        if held_keys['d']:
            self.logic.car.rotation_y -= self.turn_speed

        camera.position = self.logic.car.position + Vec3(0, 6, -15)
        camera.look_at(self.logic.car)

# Main loop
def main():
    app = Ursina()
    game = CarGameFrontend()
    app.run()

if __name__ == '__main__':
    main()
