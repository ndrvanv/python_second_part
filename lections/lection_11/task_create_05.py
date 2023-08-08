class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Create {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра{self.name = } ')

u_1 = User('Spengler')
u_2 = User('Venkman')