
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(*t)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
    print(e) # red green blue

# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)