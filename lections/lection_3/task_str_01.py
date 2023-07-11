text = 'Hello world!'
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2) #Строка не изменяемый объект при изиенение значения создается новый объект в памяти
print(text, new_txt, sep='\n')