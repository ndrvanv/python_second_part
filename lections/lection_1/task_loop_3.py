min_limit = 0
max_limit = 10
while True:
    print("Введите число между ", min_limit, " и ", max_limit, " ?")
    num = float(input())
    if num < min_limit or num > max_limit:
        print("Wrong")
    else:
        break
print("Было введено число ", num)