""" 
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""

names = ['Ivan', 'Petr', 'Anton']
salaries = [10_000, 15_000, 12_500]
awards = ['10.25%', '10.25%', '10.25%']


def auxiliary_func(my_list: list[str]) -> list[float]:
    res_list = []
    for i in my_list:
        res_list.append(float(i[:-1]))
    return res_list

awards = auxiliary_func(awards)

print(*({name: (salary * award + salary) / 10} for name, salary, award in zip(names, salaries, awards)))
# мне не нравится, что в строке много символов, но ТЗ есть ТЗ...