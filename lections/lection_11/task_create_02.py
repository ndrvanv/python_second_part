class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Create{self.name = }')

    def __new__(cls, *args, **kwargs):
        isinstance = super().__new__(cls)
        print(f'Create class {cls}')
        return isinstance
    

print('Create first time')
u_1 = User('Spengeler')
print('Create second time')
u_2 = User('Venkman')
print('Create third time')
u_3 = User(name='Stenc')