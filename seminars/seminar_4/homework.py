import numpy as np


# Напишите функцию для транспонирования матрицы
# mat = [
#     [2, 3, 5],
#     [23, 4, 6],
#     [7, 8, 9]
# ]
# print(np.array(mat))
# print()
#
#
# def matrix(matrix: list):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     result = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(matrix[j][i])
#         result.append(row)
#     return result
#
#
# a = np.array(matrix(mat))
# print(a)


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# def funct(**kargs):
#     dict = {}
#     for key, value in kargs.items():
#         if isinstance(value, str):
#             dict[value] = key
#         else:
#             dict[str(value)] = key
#     return dict
#
#
# result = funct(a=1, b='test', c=[1, 2, 4])
# print(result)

# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

wallet = 1500
currency = 'rub'
name_wallet = 'Ivanov Ivan Ivanovich'

def cash_withdrawal(money_for_cash: int, wallets: int):
    global wallet
    if money_for_cash < 100:
        return 'Сумма снятия должна быть кратна сумме 100 рублей'
    if wallet < money_for_cash:
        return 'Сумма снятия наличных превышает сумму доступного!'
    else:
        wallet -= money_for_cash
        return wallet


def cash_depositing(count: int):
    global wallet
    money = int(input('Введите сумму которую вы хотите попольнить на карту: '))
    count = count + money
    return count

def switch_case():
    global wallet
    way = int(input("Выберите какую операцию вы бы хотели произвести:\n1) - Снятие наличных\n2) - Внесение средств на картрасчет:\n"))
    match way:
        case 1:
            print(cash_withdrawal(int(input('Введите сумму для снятия наличных ')), wallet))
            print(f'Ваш остаток на счету {name_wallet} {wallet} {currency}')
            return
        case 2:
            print(cash_depositing(wallet))
            print(f'Ваш остаток на счету {wallet} {currency}')

switch_case()