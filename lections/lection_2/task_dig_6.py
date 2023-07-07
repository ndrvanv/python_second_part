DEFAULT = 23
num = int(input("Введите уровень или ноль для значения по умолчанию: "))
level = num or DEFAULT
print(level)