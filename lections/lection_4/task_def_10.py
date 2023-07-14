def pos_only_arg(arg, /):
    # Пример только позиционной функции
    print(arg)

pos_only_arg(42)
# вывод: "42"

def pos_only_arg_2(*, arg):
    # Пример только ключевой функции
    print(arg) #Принт как пример

pos_only_arg_2(arg=42)
# вывод: "42"

def combined_example(pos_only, /, standart, *, kwd_only):
    #Пример функции со всеми вариантами параметров
    print(pos_only, standart, kwd_only) #Print only like example

combined_example(1, 2, kwd_only=3)
combined_example(1, standart=2, kwd_only=3)

# def func(*args): — принимает любое число позиционных аргументов
# def func(**kwargs): — принимает любое число ключевых аргументов
# def func(*args, **kwargs): — принимает любое число позиционных и ключевых аргументов