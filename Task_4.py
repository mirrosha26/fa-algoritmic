class Order:
    def __init__(self, vendor_code: str, price: float, count: int):
        self.vendor_code = vendor_code
        self.price = price
        self.count = count

    def __str__(self):
        return f'product {self.vendor_code} ({self.price} руб. X {self.count} шт.)'

class Opt(Order):
    def summa(self):
        if self.count > 500:
            print(f'Скидка 10% на оптовый заказ от 500 шт. [{round(self.price*0.90, 3)} руб./шт.]')
            return round(self.price * self.count* 0.9,2)
        print(f'Скидка 5% на оптовый заказ. [{round(self.price*0.95, 2)} руб./шт.]')
        return round(self.price * self.count* 0.95,2)


class Retail(Order):
    def summa(self):
        return round(self.price * self.count,2)

if __name__ == "__main__":
    print("Создаем заказ на ручки")
    pen = Order( "00001",14.2,6)
    print(pen)

    print("Заказ ручек в розницу")
    pen_ret = Retail("00001",14.2,6)
    print(f'{pen_ret} =  {pen_ret.summa()}')
    pen_ret.count = 7  
    print(f'{pen_ret} = {pen_ret.summa()}')

    print("Заказ ручек оптом")
    pen_ret = Opt("00001",14.2,20)
    print(f'{pen_ret} =  {pen_ret.summa()}')
    pen_ret.count = 550
    print(f'{pen_ret} = {pen_ret.summa()}')