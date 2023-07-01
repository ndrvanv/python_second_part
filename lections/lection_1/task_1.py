name = 'Alex'
age = None

a = 42
print(id(a))
a = "Hello world"
print(id(a))
a = 3.14 / 3
print(id(a)) 

print(name, age, a, 123, 'text', sep=' (=^.^=) ', end='#')
print('Any text')

result = input('Print your text: ')
print('You wrote', result)

ADULT = 18
age = int(input('Сколько тебе лет? '))

how_old = ADULT - age
print(how_old, ' лет осталось до совершеннолетия')