SIZE = 100
with open('C:/Users/1311103/OneDrive/Рабочий стол/GB/python_2/lections/lection_7/text_data.txt','r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)