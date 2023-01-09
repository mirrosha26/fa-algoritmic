'''
Создайте класс Point (точка), у которого имеются:
- 2 атрибута x и y (координаты)
- методы __init__() и __str__(),

Класс Rect (прямоугольник), у которого есть: 
- два атрибута (верхний левый угол и правый нижний угол прямоугольника). 

Значениями атрибутов являются объекты класса Point; 
- методы __init__() и __str__();
- метод sides(), возвращающий длины сторон прямоугольника; 
- метод perim(), вычисляющий периметр прямоугольника. 

Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

# в __init__ передаем объекты класса Point
class Rect:
    def __init__(self, upper_left_corner, bottom_right_corner):
        self.upper_left_corner = upper_left_corner
        self.bottom_right_corner = bottom_right_corner

    def __str__(self):
        return f'Rectangle: [{self.upper_left_corner} ⟍ {self.bottom_right_corner}]'

    def sides(self):
        self.length = - self.upper_left_corner.x + self.bottom_right_corner.x
        self.height = self.upper_left_corner.y - self.bottom_right_corner.y
        return {
            'length': self.length,
            'height': self.height
        }

    def perim(self):
        return 2*sum(self.sides().values())

if __name__ == '__main__':
    print("Создаем две новые точки: ")
    a = Point(2,4)
    print(f'* Точка A: {a}')
    print(f'\tКооридината х: {a.x}')
    print(f'\tКооридината y: {a.y}')
    b = Point(8,0)
    print(f'* Tочка B: {b}')
    print(f'\tКооридината х: {b.x}')
    print(f'\tКооридината y: {b.y}')
    print()
    print('Создаем прямоугольник:')
    rect_ab = Rect(a,b)
    print(f'\t{rect_ab}', end="\n\n")
    print(f'Получаем длины сторон: \n\t{rect_ab.sides()}')
    print(f'\tДлина: {rect_ab.length}')
    print(f'\tВыстоа: {rect_ab.height}\n')
    print("Периметр прямоугольника:")
    print(rect_ab.perim())

