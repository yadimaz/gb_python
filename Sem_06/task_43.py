"""Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
"""
#from functions import create_list

list1 = [1, 2, 3, 2, 3, 3, 3, 3]
# Создаём словарь dict1, где ключами являются не дублирующиеся элементы списка list1, с помощью функции set,
# а значения будут показывать сколько раз ключи всречались в списке list1
dict1 = {key: 0 for key in set(list1)}
print(dict1)

for el in list1:
    for key in dict1:
        if el == key:
            dict1[el] += 1
print(dict1)

count = 0
# Проверяем значения ключей на чётность
for key, value in dict1.items():
    count += value // 2
print(count)

# print(sum([nums.count(item) // 2 for item in set(nums)]))