class SinglDirect:
    def __init__(self, value):
        self.__next = None
        self.__value = value
        self.head = self

    def __str__(self):
        return f'{self.__value} --> {self.__next}'
    
    def get(self):
        return self.__value

    def change(self, new_value):
        self.__value = new_value
        return self.__value

    def next(self):
        return self.__next

    def append(self, value):
        end = SinglDirect(value)
        n = self
        while (n.__next):
            n = n.__next
        n.__next = end
        n.__head = self


test = SinglDirect(1)
test.append(2)
test.append(4)
print(test.get())
test.change(6)
h = test.next()
print(h)
print(test)