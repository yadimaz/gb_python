"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
data = [5, 1, 6, 5, 9]
# list(map(int, input("Введите числа через пробел: ").split()))
max_num = data[0]
min_num = data[0]


for el in data:
    if el > max_num:
        max_num = el
    if el < min_num:
        min_num = el

print(min_num, max_num)

def func(data=[5, 1, 6, 5, 9], max_num=data[0], min_num=data[0]):
    if len(data) == 0:
        return max_num, min_num
    if data[0] > max_num:
        max_num = data[0]
    if data[0] < min_num:
        min_num = data[0]
    return func(data[1:], max_num, min_num)

print(func(data))