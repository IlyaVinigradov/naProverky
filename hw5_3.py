""" 
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def gen_fibonacci(amount):
    start = 0
    next_num = 1
    for i in range(amount):
        temp = next_num
        next_num = start + next_num
        start = temp
    yield next_num

for i, num in enumerate(gen_fibonacci(10)):
    print(f'{num}')
