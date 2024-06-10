"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
Посмотреть сколько в нем строк и столбцов
Определить какой тип данных имеют столбцы
"""
from pandas import read_csv

data = read_csv('california_housing_test.csv')

# Посмотреть сколько в нем строк и столбцов
print(data.shape)

# Определить какой тип данных имеют столбцы
print(data.dtypes)

print(data.info())

print(data.describe())
