'''
Создайте класс Point (точка),
у которого имеются 2 атрибута x и y (координаты)
и методы __init__() и __str__()

класс Treyg (треугольник), у которого есть: 
• три атрибута (верхушки треугольника). 
    Значениями атрибутов являются объекты класса Point; 
• методы __init__() и __str__(); 
• метод sides(), возвращающий длины сторон треугольника; 
• метод perim(), вычисляющий периметр треугольника. 

Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

# в __init__ передаем объекты класса Point
class Treyg:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return f'Triangle ({self.A}, {self.B}, {self.C})'

    def length(self, point_0, point_1):
        length = ((point_1.x - point_0.x)**2 + (point_1.y - point_0.y)**2)**0.5
        return  round(length,2)

    def sides(self):
        self.AB = self.length(self.A, self.B)
        self.BC = self.length(self.B, self.C)
        self.CA = self.length(self.C, self.A)
        return {
            'AB': self.AB,
            'BC': self.BC,
            'CA': self.CA
        }

    def perim(self):
            return round(sum(self.sides().values()),2)


if __name__ == '__main__':
    print("Создаем три точки: ")
    A = Point(-5,3)
    print(f'* Точка A: {A}')
    print(f'\tКооридината х: {A.x}')
    print(f'\tКооридината y: {A.y}')
    B = Point(-2,1)
    print(f'* Tочка B: {B}')
    print(f'\tКооридината х: {B.x}')
    print(f'\tКооридината y: {B.y}')
    C = Point(2,0)
    print(f'* Tочка B: {C}')
    print(f'\tКооридината х: {C.x}')
    print(f'\tКооридината y: {C.y}')
    print()
    
    print('Создаем треугольник ABC:')
    Triangle_ABC = Treyg(A,B,C)
    print(f'\t{Triangle_ABC}', end="\n\n")
    print(f'Получаем длины сторон: \n\t{Triangle_ABC.sides()}')
    print(f'\tДлина: {Triangle_ABC.AB}')
    print(f'\tДлина: {Triangle_ABC.BC}')
    print(f'\tВыстоа: {Triangle_ABC.CA}\n')
    print(f'Периметр прямоугольника:{Triangle_ABC.perim()}')
