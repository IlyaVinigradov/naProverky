""" 
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

my_line = '/Users/umpabook/src/Python/web/5/home_work5/hw5_1.py'


def my_path(line: str):
    result = []
    result.append(str(line))
    line = line.split('/')
    line = str(line.pop(-1))
    line = line.split('.')
    result.append(line.pop(-2))
    result.append(line.pop())
    return result


print(my_path(my_line))
