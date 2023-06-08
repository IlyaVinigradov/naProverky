"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import datetime


class My_str(str):
    """ класс Моя Строка, где:
    доступны все возможности str
    дополнительно хранятся имя автора строки и время создания """

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance._name = name
        instance._time = datetime.datetime.now()
        return instance

    def get_name(self):
        return self._name
    
    def get_time(self):
        return self._time

    def __str__(self) -> str:
        return f'{super().__str__()} {self.get_name()} {self.get_time()}'

    # def __repr__(self) -> str:
    #     return f'My_str({cls.super().value}, {self._name})'
    

if __name__ == '__main__':
    my_str = My_str('test', 'test_name')

    print(my_str)
    print(repr(my_str))
    help(My_str)