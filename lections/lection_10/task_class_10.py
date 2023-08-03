class Person:
    max_up = 3
    
    def __init__(self, name, race = 'unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

p1 = Person('Нирвана', 'Эльф')
p2 = Person('Фил', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')