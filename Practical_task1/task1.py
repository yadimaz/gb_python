"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.

Пример:
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)

При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`
При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

n = 123

# Введите ваше решение ниже

res = n // 100 + n % 100 // 10 + n % 10
print(res)