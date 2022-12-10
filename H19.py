class Mod:
    def __init__(self, a: int, m:int):
        # a mod m
        if m < 2:
            raise Exception('Введеный модуль меньше двух')
        self.a =a 
        self.m = m
        self.rem = a % m

    def __str__(self):
        #return f'{self.a} mod {self.m} = {self.rem}'
        return f'{self.a} mod {self.m}'

    def __add__(self, b):
        #(a+b)mod_m ==(a mod_m + b mod_m)mod_m,
        if not isinstance(b, Mod):
            #raise Exception('Объект суммы не является объектом класса Mod')
            print('Объект суммы не является объектом класса Mod')
            return None
        if self.m != b.m:
            print('Объект суммы не является объектом класса Mod')
            print('модули не равны')
            return None
        return Mod((self.rem + b.rem)%a.m, a.m)


    def __sub__(self, b):
        if not isinstance(b, Mod):
            #raise Exception('Объект разности не является объектом класса Mod')
            print('Объект разности не является объектом класса Mod')
            return None
        if self.m != b.m:
            print('модули не равны')
            return None
        return Mod((self.rem - b.rem)%a.m, a.m)
    

a = Mod(15,7)
b = Mod(17,7)
print(a + b)
print(a - b)