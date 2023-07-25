
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы
# они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь
# пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
# друга верните истину, а если бьют - ложь

def is_attack(x1, y1, x2, y2):
    # Проверка того что бьют ли ферзи по вертикали, по горизонтали или по диаганали
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def has_attacing_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if is_attack(x1, y1, x1, y2):
                return True
    return False

queens = []
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

result = has_attacing_queens(queens)
print(result)
