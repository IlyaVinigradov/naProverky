""" 
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды
"""

my_list = [1, 2, 3, 4, 5, 1, 4, 6, 6, 7]
print(my_list)

temp = set(my_list)
s = set()
for i in my_list:
    if my_list.count(i) > 1:
        s.add(i)

res = temp - s
print(res)