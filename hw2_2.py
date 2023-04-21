""" 
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

import fractions


fraction_1 = input()
fraction_2 = input()
print()


def sum(fraction1, fraction2):
    fraction1 = list(map(int, fraction1.split('/')))
    fraction2 = list(map(int, fraction2.split('/')))
    sum = fraction1[0] / fraction1[1] + \
        fraction2[0] / fraction2[1]
    return sum


print(sum(fraction_1, fraction_2))


def sum_frac(fraction1, fraction2):
    fraction1 = fraction1.split('/')
    fraction2 = fraction2.split('/')
    f1 = fractions.Fraction(int(fraction1[0]), int(fraction1[1]))
    f2 = fractions.Fraction(int(fraction2[0]), int(fraction2[1]))
    return f1 + f2


print(sum_frac(fraction_1, fraction_2))
a = list(map(int, str(sum_frac(fraction_1, fraction_2)).split('/')))
print(a[0] / a[1])
print()


def mult(fraction1, fraction2):
    fraction1 = list(map(int, fraction1.split('/')))
    fraction2 = list(map(int, fraction2.split('/')))
    mult = fraction1[0] / fraction1[1] * fraction2[0] / fraction2[1]
    return mult


print(mult(fraction_1, fraction_2))


def mult_frac(fraction1, fraction2):
    fraction1 = fraction1.split('/')
    fraction2 = fraction2.split('/')
    f1 = fractions.Fraction(int(fraction1[0]), int(fraction1[1]))
    f2 = fractions.Fraction(int(fraction2[0]), int(fraction2[1]))
    return f1 * f2


print((mult_frac(fraction_1, fraction_2)))
a = list(map(int, str(mult_frac(fraction_1, fraction_2)).split('/')))
print(a[0] / a[1])