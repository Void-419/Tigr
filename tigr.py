import random
import time

class Field:
    def __init__(self, size):
        self.size = size
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)
        self.tiger = Tiger()
        self.rabbit1 = Rabbit()
        self.rabbit2 = Rabbit()
        self.grid[self.tiger.y][self.tiger.x] = self.tiger
        self.grid[self.rabbit1.y][self.rabbit1.x] = self.rabbit1
        self.grid[self.rabbit2.y][self.rabbit2.x] = self.rabbit2

    def display(self):
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None:
                    display_row += ". "
                elif isinstance(cell, Rabbit):
                    display_row += "З "
                else:
                    display_row += "Т "
                    cell.update([self.grid[self.rabbit1.y][self.rabbit1.x], self.grid[self.rabbit2.y][self.rabbit2.x]])
            print(display_row)

class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"
        self.x = 0
        self.y = 0

    def update(self, rabbits):
        if self.state == "Выследить добычу":
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)
            for rabbit in rabbits:
                if self.x - rabbit.x == 1 and self.y - rabbit.y == 1:
                    self.state = "Атаковать добычу"
        if self.state == "Атаковать добычу":
            i = random.randint(0, 1)
            if i == 1:
                print("Заяц был пойман")
                self.attack(rabbits)
            else:
                print("Заяц убежал")

    def attack(self, rabbits):
        for rabbit in rabbits:
            if self.x - rabbit.x == 1 and self.y - rabbit.y == 1:
                self.state = "Бежать домой"
                del rabbit

class Rabbit:
    def __init__(self):
        while True:
            self.x = random.randint(0, 4)
            self.y = random.randint(0, 4)
            if self.x != 0 or self.y != 0:
                break

field = Field(5)

while True:
    field.display()
    time.sleep(1)