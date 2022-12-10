import random
import time

class Sensor:
    ClassName = "Sensor"

    def __init__(self):
        self.exit = self.get()
    
    def __str__(self):
        return f'{ self.ClassName }: {self.exit}'

    def get(self):
        return None

class Anemometer(Sensor):
    ClassName = "Anemometer"

    def get(self):
        self.exit = round(random.uniform(0, 3)/3,2)
        return self.exit

class Hygrometer(Sensor):
    ClassName = "Hygrometer"

    def get(self):
        self.exit = round(random.uniform(0, 2)/2,2)
        return self.exit

if __name__ == "__main__":
    print("Создадим несколько датчиков")
    anemometer_1 = Anemometer()
    hygrometer_1 = Hygrometer()
    print(anemometer_1)
    print(hygrometer_1)

    print('Получаем 10 измерений с датчиков с задержкой в 1 сек')
    for i in range(10):
        print(f'Anemometer_1: {anemometer_1.get()}')
        print(f'Hygrometer_1: {hygrometer_1.get()}')
        time.sleep(1)

    print('Получаем полследние измерения:')
    print(f'Anemometer_1: {anemometer_1.exit}')
    print(f'Hygrometer_1: {hygrometer_1.exit}')