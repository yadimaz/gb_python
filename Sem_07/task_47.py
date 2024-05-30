"""
У вас есть код, который вы не можете менять (так часто бывает, когда код
в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))

Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.
"""

transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # или любой другой список
transormed_values = list(map(transformation, values))

if values == transormed_values:
    print("ok")
else:
    print("not ok")
