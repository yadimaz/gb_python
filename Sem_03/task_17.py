"""
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
from typing import List

list_in = [1, 1, 2, 0, -1, 3, 4, 4]
uniq_list = []
for el in list_in:
    if el not in uniq_list:
        uniq_list.append(el)
print(len(uniq_list))
