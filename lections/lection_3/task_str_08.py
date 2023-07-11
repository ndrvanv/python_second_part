link = 'https://habr.com/ru/articles/747164/'
urls = link.split('/')
print(urls)

a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите не менее трех чисел через пробел: ').split()