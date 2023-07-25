import random
#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

def generate_queens_random(num_queens):
    queens = []
    for _ in range(num_queens):
        queens.append((random.randint(0, num_queens - 1), random.randint(0, num_queens - 1)))
    return queens

def is_valid_solution(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0] == abs(queens[i][1] - queens[j][1])):
                return False
        return True

def find_succesful_move(num_queens, num_solution):
    succeful_solution = []
    while len(succeful_solution) < num_solution:
        queens = generate_queens_random(num_queens)
        if is_valid_solution(queens):
            succeful_solution.append(queens)
    return succeful_solution

num_queens = 8
num_solutions = 4
succeful_move = find_succesful_move(num_queens, num_solutions)

for i, solution in enumerate(succeful_move):
    print(f"Расстановка ферзей {i + 1}: ")
    for queen in solution:
        print(queen)
    print()