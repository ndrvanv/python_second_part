import os
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# def file_tuple(file_path):
#     file_name = os.path.basename(file_path)
#     path = os.path.dirname(file_path)

#     file_name_parts = os.path.splitext(file_name)
#     file_name_without_extension = file_name_parts[0]
#     file_extension  = file_name_parts[1]

#     return path, file_name_without_extension, file_extension

# file_path = "file.txt"

# path, file_name, file_extension = file_tuple(file_path)

# print('Путь файла ', path)
# print('Имя файла ', file_name)
# print('Расширение файла ', file_extension)


#Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Olya', 'Tanya', 'Leo']
awards = [200, 410, 350]
rates = ['12.5%', "5.5%", "8.3%"]

result = {name: award * float(rate.strip("%")) / 100 for name, award, rate in zip(names, awards, rates)}
print("Словарь:", result)
print()

# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacii_generator():
    a, b = 0, 1
    while True:
        yield a
        a,b=b,a+b

fib = fibonacii_generator()
for i in range(12):
    print(next(fib))