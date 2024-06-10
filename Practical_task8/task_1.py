"""
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists

"""
Создать телефонный справочник с
возможностью импорта и экспорта данных вS
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists


class NameError(Exception):
    def init(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()


def new_item(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    write_file(file_name, res)


def write_file(file_name, str):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(str)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)  # ящик со словарями


def print_list(f_r):
    i = 1
    for line in f_r:
        print(f"{i}. {line['first_name']} {line['second_name']} {line['phone_number']}")
        i += 1


def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    res.pop(search - 1)
    write_file(file_name, res)


def copy_row(file_name):
    search = int(input('Введите номер строки для копирования: '))
    res1 = read_file(file_name)
    res2 = read_file(file_copy)
    res2.append(res1[search - 1])
    write_file(file_copy, res2)

def copy_data(file_name):
    f_copy = read_file(file_name)
    write_file(file_copy, f_copy)


file_name = 'phone.csv'
file_copy = 'phone2.csv'


def main():
    while True:

        command = input('\nh - список команд\nВведите команду: ')
        if command == 'q':
            break
        elif command == 'h':
            print("\nСписок команд:\nw - запись в справочник, создание справочника\nr - чтение справочника\nd - "
                  "удаление строки из справочника\nc - резервная копия справочника\nrc - прочитать копию "
                  "справочника\nq - выход\ncr - копировать строку")
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            new_item(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, пожалуйста , создайте файл')
                continue
            # print(*read_file(file_name))
            print_list(read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('Файл отсутствует, пожалуйста , создайте файл')
                continue
            remove_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('Файл отсутствует, пожалуйста , создайте файл')
                continue
            copy_data(file_name)
        elif command == 'rc':
            if not exists(file_copy):
                print('Файл отсутствует, пожалуйста , создайте файл')
                continue
            print_list(read_file(file_copy))
        elif command == 'cr':
            if not exists(file_name):
                print('Файл отсутствует, пожалуйста , создайте файл')
                continue
            copy_row(file_name)


main()

"""
реализовать копирование данных из файла А в файл B.
написать отдельную функцию copy_data:
прочитать список словарей (read_file)
и записать его в новый файл используя функцию standart_write
дополнить функцию main
"""
