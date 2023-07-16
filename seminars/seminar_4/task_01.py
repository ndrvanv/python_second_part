"""✔Напишите функцию, которая принимает строку текста. 
Вывести функцией каждое слово с новой строки. ✔Строки нумеруются начиная с единицы. 
✔Слова выводятся отсортированными согласно кодировки Unicode. 
✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
"""

def str_printer(str_input):
    res = ''
    str_input = str_input.split()
    str_input.sort()
    maxx = max([len(i) for i in str_input])
    for n, s in enumerate(str_input, 1):
        res = res + (f"{n} {s:>{maxx}}\n")
    return res

print(str_printer('Карл у Клары украл кораллы'))

"""✔Напишите функцию, которая принимает строку текста. 
✔Сформируйте список с уникальными кодами Unicode каждого 
символа введённой строки отсортированный по убыванию."""

def to_ord(string):
    return sorted(set(map(ord, list(string))), reverse = True)


to_ord = lambda x: sorted(set(map(ord, list(x))), reverse = True)

"""✔Функция получает на вход строку из двух чисел через пробел. 
✔Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число. 
✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно."""

def make_dict(str_input:str):
    beg,end=sorted(str_input.split())
    # dict={ord(x):x for x in range(int(beg),int(end))}
    return {ord(str(x)):x for x in range(int(beg),int(end)+1)}

print(make_dict('7 3'))

"""✔Функция получает на вход список чисел. 
✔Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии."""

str_size = 10

def buble_sort(sorted_list):
    for i in range(str_size):
        for j in range(str_size - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]


print(my_list := [randint(0, 100) for i in range(str_size)])
buble_sort(my_list)
print(my_list)

"""✔Функция принимает на вход три списка одинаковой длины: ✔имена str, 
✔ставка int, ✔премия str с указанием процентов вида «10.25%». 
✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. 
✔Сумма рассчитывается как ставка умноженная на процент премии."""

from pprint import pprint

def grants_dict(names, pays, percents):
    percents  = list(map(lambda x: float(x[:-1])/100, percents))
    return {name: pay*percent for name, pay, percent in zip(names, pays, percents) }

names = ['Иван', "Петр", "Михаил"]
pays = [10000, 15000, 20000]
percents = ['50.25%', "20%", "30.6%"]


pprint(grants_dict(names, pays, percents))

"""✔Функция получает на вход список чисел и два индекса. 
✔Вернуть сумму чисел между между переданными индексами. 
✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка."""

def is_all_rentable(companies):
    return all([sum(i) > 0 for i in companies.values()])

dict_companies = {}

company_names = ["aaa", "bbb", "ccc"]
aaa_digit = [10, -20, 30, 40]
bbb_digit = [21, 212, -44]
ccc_digit = [333, -3333, 22222]

dict_companies[company_names[0]] = aaa_digit 
dict_companies[company_names[1]] = bbb_digit 
dict_companies[company_names[2]] = ccc_digit

print(is_all_rentable(dict_companies))

"""✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
(кроме переменной из одной буквы s) на None. ✔Значения не удаляются, 
а помещаются в одноимённые переменные без s на конце."""

numbers = [1, 2, 3]
s = 'super'
letter = 'a'

def rename():
    variables = globals()
    temp = {}
    for key, value in variables.items():
        if len(key) > 1 and key.endswith('s'):
            temp[key[:-1]] = variables[key]
            temp[key] = None
    variables.update(temp)
        
rename()


print({key: values for key, values in locals().items() if not key.startswith('__')})

