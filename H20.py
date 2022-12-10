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

    def __add__(self, other):
        #(a+b)mod_m ==(a mod_m + b mod_m)mod_m,
        if not isinstance(other, Mod):
            #raise Exception('Объект суммы не является объектом класса Mod')
            return None
        if self.m != other.m:
            return None
        return Mod((self.rem + other.rem)%a.m, a.m)

    def __eq__(self, other):
        if not isinstance(other, Mod):
            #raise Exception('Объект разности не является объектом класса Mod')
            return None
        return self.rem == other.rem

    def __sub__(self, other):
        if not isinstance(other, Mod):
            #raise Exception('Объект разности не является объектом класса Mod')
            return None
        if self.m != other.m:
            return None
        return Mod((self.rem - other.rem)%a.m, a.m)

    def back(self):
        #(x∗x^(-1))mod_m= 1.
        unit = Mod(1,self.m)
        for i in range(1, self.m):
            try_ex = Mod(i,self.m)
            res = self.__mul__(try_ex)
            if unit == res:
                return try_ex
        return None


    def __mul__(self, other):
        #(a ∗ b)mod_m==(a mod_m ∗ b mod_m)mod_m
        if not isinstance(other, Mod):
            return None
        if self.m !=other.m:
            return None
        return Mod((self.rem * other.rem)%a.m, a.m)

    def __truediv__(self, other):
        #(a / b)mod_m = ( a*(b^−1))mod_m.
        if not isinstance(other, Mod):
            return None
        if self.m !=other.m:
            return None

        res = self.__mul__(other.back())
        if res == None:
            return None
        return res
    

a = Mod(15,7)
b = Mod(17,7)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b / a)
