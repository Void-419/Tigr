import random
import time

class Field:
    def __init__(self, size): # конструктор класса Field
        self.size = size

        self.tiger = Tiger()
        self.rabbit1 = Rabbit()
        self.rabbit2 = Rabbit()

    def display(self): # метод для отображения зайцев и тигра
        self.tiger.update([self.rabbit1, self.rabbit2])
        for y in range(self.size):
            display_row = ""
            for x in range(self.size):
                if self.rabbit1.x == x and self.rabbit1.y == y and self.rabbit1.is_alive == True: # отображение зайцев при том условии, если они живы
                    display_row += "З "
                elif self.rabbit2.x == x and self.rabbit2.y == y and self.rabbit2.is_alive == True:
                    display_row += "З "
                elif self.tiger.x == x and self.tiger.y == y: # отображение тигра
                    display_row += "Т "
                else:
                    display_row += ". "

            print(display_row)
        print(self.tiger)
        print(self.rabbit1)
        print(self.rabbit2)


class Tiger:
    def __init__(self): # конструктор класса Tiger
        self.state = "Выследить добычу"
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Тигр x:{self.x} y:{self.y}" # информация о том, где находится тигр


    def update(self, rabbits): # метод для отслеживания 3-х состояний тигра
        if self.state == "Выследить добычу":
            self.x += random.randint(-1, 1)
            if self.x < 0:
                self.x = 0
            if self.x > 4:
                self.x = 4
            self.y += random.randint(-1, 1)
            if self.y < 0:
                self.y = 0
            if self.y > 4:
                self.y = 4
            for rabbit in rabbits:
                if abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1:
                    self.state = "Атаковать добычу"
        elif self.state == "Атаковать добычу":
            i = random.randint(0, 1)
            if i == 1:
                print("Заяц был пойман")
                self.attack(rabbits)
            else:
                print("Заяц убежал")
        elif self.state == "Бежать домой":
            self.run_in_home()

    def attack(self, rabbits):
        for rabbit in rabbits:
            if abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1:
                self.state = "Бежать домой"
                rabbit.is_alive = False

    def run_in_home(self): # метод для возвращения тигра в исходную точку
        self.x = 0
        self.y = 0



class Rabbit:
    def __init__(self): # конструктор класса Rabbit
        self.is_alive = True
        while True:
            self.x = random.randint(0, 4)
            self.y = random.randint(0, 4)
            if self.x != 0 or self.y != 0:
                break

    def __str__(self):
        return f"Заяц x:{self.x} y:{self.y}" # информация о том, где находятся зайцы


field = Field(5)

while field.tiger.state != "Бежать домой": # цикл для прорисовки поля
    field.display()
    time.sleep(1)

field.display()