"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print(f"Сгенерированный DataFrame\n{data.head()}")

# one-hot кодирования с get_dummies
print(f"\none-hot кодирования с get_dummies\n{pd.get_dummies(data, columns=['whoAmI']).head()}")

# one-hot кодирование без get_dummies
date_one_hot = pd.DataFrame()
unique_values = data['whoAmI'].unique()
# Создание столбцов для каждого уникального значения и заполнение их 0 или 1
for value in unique_values:
    date_one_hot[value] = [1 if x == value else 0 for x in data['whoAmI']]

# Вывод результата
print(f"\none-hot кодирование без get_dummies\n{date_one_hot.head()}")
