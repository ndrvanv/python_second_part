
# Класс принимает тип животного (название одного из созданных классов)
#и параметры для этого типа.
#○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Animal:
    def create_animal(self, animal_type, name, age):
        if animal_type == "Рыба":
            return Fish(name, age)
        elif animal_type == 'Птица':
            return Bird(name, age)
        elif animal_type == 'Млекопитиющее':
            return Mammal(name, age)
        else:
            raise ValueError('Error animal')
    
class Fish(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print(f'{self.name} is swimming in the pool')

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        print(f'{self.name} is flies in the sky')

class Mammal(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} is walking on the ground')

animal_factory = Animal
fish = animal_factory.create_animal("Рыба", 'Garry', 1)
fish.swim

bird = animal_factory.create_animal('Птица', "Chizhik", 2)
bird.fly()

mammal = animal_factory.create_animal('Млекопитающее', 'Мука', 6)