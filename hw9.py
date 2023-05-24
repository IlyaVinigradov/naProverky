"""
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
"""
from typing import Callable
import csv
import json
from random import randint
import math


def deco_csv(func: Callable):
    def wrapper(file) -> list:
        result = []
        with open(file, 'r', newline='') as f:
            for i in f:
                a, b, c = i.split(',')
                result.append(func(int(a), int(b), int(c)))
                # print(result)
        
        return result
    return wrapper

def deco_json(file):
    def wrapper(func: Callable) -> dict:
        with open(file, 'r') as f:
            my_dict = {}
            for i in f:
                a, b, c = map(int, i.split(','))
                my_dict[i] = func(a, b, c)
        with open('result.json', 'w') as f:
            json.dump(my_dict, f)
        return my_dict
    return wrapper


def gen_csv(amount: int):
    with open('my_gen_csv.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(amount):
            all_data = []
            all_data.append(randint(-1000, 1001))
            all_data.append(randint(-1000, 1001))
            all_data.append(randint(-1000, 1001))
            writer.writerow(all_data)


def quadratic_equations(a: int | float, b: int | float, c: int | float):
    if a == 0:
        x = -c/b
        return x
    elif b == 0:
        x1 = (-c/a)**0.5
        x2 = -1 * x1
        return (x1, x2)
    elif c == 0:
        x1 = 0
        x2 = -b/a
        return (x1, x2)
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            return (x1, x2)
        elif discriminant == 0:
            x = -b / (2*a)
            return x
        else:
            return None


if __name__ == '__main__':
    gen_csv(100)
    deco_csv(quadratic_equations)('my_gen_csv.csv')
    deco_json('my_gen_csv.csv')(quadratic_equations)