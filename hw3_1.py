""" 
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""

list_1 = [1, 3, 5, 10, 17, 3, 5, 24, 1, 10, 17, 9, 8, 7, 6]


def my_sort_list(li):
    result = set()
    for i in li:
        if li.count(i) != 1:
            result.add(i)
    return result


print(my_sort_list(list_1))
