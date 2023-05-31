"""
Доработаем задачи 5-6. Создайте класс-фабрику.
    ○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
    ○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""
from sem10_6 import animal, fish, bird, mammal


class Fabric:

    def __init__(self, type: type, *args) -> object:
        if type == animal.Animal:
            return animal.Animal(*args)
        elif type == fish.Fish:
            return fish.Fish(*args)
        elif type == bird.Bird:
            return bird.Bird(*args)
        elif type == mammal.Mammal:
            return mammal.Mammal(*args)
        else:
            return None
        

    # def specific(self):
    #     type.specific()


if __name__ == '__main__':
    fab = Fabric(fish, 'fish')

    # по тз не требовалось, но всплывает ошибка
    # fab.specific() # File "/Users/umpabook/src/Python/web/10/hw10/hw10_1/Fabric.py", line 33, in <module>
#     fab.specific()
# AttributeError: 'Fabric' object has no attribute 'specific'
