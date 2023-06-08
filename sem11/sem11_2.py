"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""

""" Добавьте к задачам 1 и 2 строки документации для классов. """


class Archive:
    """ класс Архив, который хранит пару свойств """

    _instance = None
    

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._my_list = list()
        else:
            cls._instance._my_list.append((cls._instance.number, cls._instance.some_str))
        return cls._instance

    def __init__(self, number, some_str):
        self.number = number
        self.some_str = some_str
    
    def __str__(self) -> str:
        return f'{self.number = }, {self.some_str = }, {self._my_list = }'


if __name__ == '__main__':
    arc1 = Archive(33, 'str')
    print(arc1)
    arc2 = Archive(44, 'str2')
    print(arc2)
    arc3 = Archive(55, 'str3')
    print(arc3)
    help(Archive)