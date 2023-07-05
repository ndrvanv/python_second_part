# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
#“Число является простым, если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч

number = int(input("Введите целочисленное число больше 0 и не более 100,000: "))
START_NUMBER = 2
isPrime = False
if number < 0 or number > 100000:
    print("Вы вышли за гранью диапазона")
else:
    for i in range(START_NUMBER, number):
        if number % i != 0:
            isPrime = True
        elif number % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print("Простое число")
    elif isPrime == False:
        print("Составное число")