import pyxel
from main import *
from parser import *

class App:
    def __init__(self):
        self.venue = parse('venue.json')
        pyxel.init(self.venue.x_max, self.venue.y_max)
        self.counter = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        for person in self.venue.persons:
            person.move()

    def draw(self):
        pyxel.cls(0)

        for person in self.venue.persons:
            if not person.done:
                pyxel.rect(person.x, person.y, 5, 5, person.color)




App()