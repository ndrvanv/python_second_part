a = 5
print(a, id(a))
a += 1
print(a, id(a))

#txt = 'Hello World'
#txt[5] = '_'
# string is immutable in python so it will raise TypeError: "str" object does not support item

txt = 'Hello world'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))