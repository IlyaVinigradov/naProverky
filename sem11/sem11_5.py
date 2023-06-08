"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""
"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

class Rectangle:
    """ класс прямоугольник """

    def __init__(self, a: int, b: int | None = None) -> None:
        self._a = a
        self._b = b

    def area(self):
        if self._a == self._b or self._b == None:
            return self._a ** 2
        else:
            return self._a * self._b

    def perimeter(self):
        if self._a == self._b or self._b == None:
            return 4 * self._a
        else: 
            return (self._a + self._b) * 2
    
    def __str__(self) -> str:
        return f'a = {self._a}, b = {self._b}'

    def __repr__(self) -> str:
        return f'Rectangle({self._a}, {self._b})'

    def __add__(self, other):
        return self.perimeter() + other.perimeter()
            
    def __sub__(self, other):
        if other.perimeter() > self.perimeter():
            return abs(self.perimeter() - other.perimeter())
        return self.perimeter() - other.perimeter()

    def __eq__(self, other) -> bool:
        return self.area() == other.area()
    
    def __ne__(self, other) -> bool:
        return self.area() != other.area()
    
    def __gt__(self, other) -> bool:
        return self.area() > other.area()
    
    def __ge__(self, other) -> bool:
        return self.area() <= other.area()
    
    def __lt__(self, other) -> bool:
        return self.area < other.area()
    
    def __le__(self, other) -> bool:
        return self.area() >= other.area()

if __name__ == '__main__':
    help(Rectangle)

    rectangle1 = Rectangle(5, 10)
    print(repr(rectangle1))
    print(rectangle1)
    print('Srectangle1 = ', rectangle1.area())
    print('Prectangle1 = ', rectangle1.perimeter())
    print()

    rectangle2 = Rectangle(5)
    print(repr(rectangle2))
    print(rectangle2)
    print('Srectangle2 = ', rectangle2.area())
    print('Prectangle2 = ',rectangle2.perimeter())
    print()

    print('Prectangle1 + Prectangle2 = ', rectangle1 + rectangle2)
    print('Prectangle1 - Prectangle2 = ', rectangle1 - rectangle2)
    print()

    rectangle3 = Rectangle(10, 10)
    rectangle4 = Rectangle(10, 10)
    print(rectangle3 == rectangle4)
    print(rectangle1 <= rectangle2)