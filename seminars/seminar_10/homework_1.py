
# Доработаем задания 5-6. Создайте класс-фабрику.
#Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Animals by name {self.name} and age {self.age}')


class Fish:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def swim(self):
        print(f'{self.name } swimming in the water')

    def info(self):
        print(f'Name is {self.name} age {self.age}')

class Bird(Animal):
    def fly(self):
        print(f'{self.name} flies in the sky')

fish_1 = Fish('Ki', 3)
fish_1.swim
fish_1.info
