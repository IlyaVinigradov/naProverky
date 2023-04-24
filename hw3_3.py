""" 
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.
"""


di = \
    {
        'tent': 10,
        'sleeping_bag': 5,
        'bowlers': 2.5,
        'cloth': 10,
        'medicine_chest': 2.5,
        'survival_kit': 3.5,
        'tools': 1.5
    }


def my_backpack(load_capacity, dict):
    for item in dict.items():
        if load_capacity - item[1] >= 0:
            load_capacity = load_capacity - item[1]
            print(f'свободного места осталось == {load_capacity}')
            print(item[0])


my_backpack(30, di)
