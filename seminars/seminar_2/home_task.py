import fractions

"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
"""
number = int(input("Введите целое число: "))
number_hex = hex(number)
print(number_hex)

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
fraction_one = fractions.Fraction(int(input("Введите первое число для дроби: ")), int(input("Введите второе число для дроби: ")))
fraction_two = fractions.Fraction(int(input("Введите первое число для дроби: ")), int(input("Введите второе число для дроби: ")))
sum_fraction = fraction_one + fraction_two
mult_fraction = fraction_one * fraction_two
print("Сумма дробей: ", sum_fraction)
print("Произведение дробей: ", mult_fraction)