import sys

text = input("Введите текст: ")
try:
    number = int(text)
    print(oct(text), hex(text), bin(text))
except ValueError:
    if all(ord(c) < 128 for c in text):
        print("Text in ascii")
    else:
        print("no ascii")