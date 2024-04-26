'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
Пример
n=16
#Вывод
1
2
4
8
16
'''
n = 1024
# en = 0
# flag = True
# while flag:
#     res = (2 ** en)
#     flag = res <= n
#     if flag:
#         print(res)
#     en += 1
#
for en in range(n):
    res = 2 ** en
    if res > n:
        break
    print(res)
