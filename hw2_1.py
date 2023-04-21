""" 
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
"""

num = int(input())

print(hex(num))


def my_hex(a):
    dict_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    li = []
    while a != 0:
        b = a % 16
        a = a // 16
        if b in dict_16:
            li.append(dict_16.get(b))
        else:
            li.append(b)
    li.reverse()
    return li


# print(''.join(my_hex(num))) почему то не переводит лист в список(((
print(my_hex(num))
