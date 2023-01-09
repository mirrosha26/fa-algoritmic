import random
import time
import datetime

class Sensor_value:

    def __init__(self, parameter):
        self.parameter = parameter
        self.date_time = datetime.datetime.now()

    def __str__(self):
        return f'{self.parameter} [{self.date_time}]'


class Sensor:
    ClassName = "Sensor"
    def __init__(self, name: str):
        self.exit = self.get()
        self.name = name
    
    def __str__(self):
        return f'{ self.ClassName } ({self.name}):\t {self.exit}'

    def get(self):
        result = self.signal() * (self.max - self.min) + self.min
        self.exit = Sensor_value(result)
        return self.exit
    
    def signal(self):
        pass

class Anemometer(Sensor):
    ClassName = "Anemometer"

    def signal(self):
        return round(random.uniform(0, 1)**2,2)

class Hygrometer(Sensor):
    ClassName = "Hygrometer"

    def signal(self):
        return round(random.uniform(0, 1),2)


class Coner(Sensor):
    ClassName = "Corner"

    def get(self):
        result = self.signal()
        self.exit = Sensor_value(result)
        return self.exit

    def signal(self):
        return round(random.uniform(0, 360),3)


if __name__ == "__main__":
    print("Задаем колиброку классам датчиков")
    Anemometer.min = 0
    Anemometer.max = 50
    Hygrometer.min = 0
    Hygrometer.max = 100
    print("Создадим несколько датчиков")
    anemometer_1 = Anemometer('Датчик в точке A')
    hygrometer_1 = Hygrometer('Датчик в точке B')
    coner_1 = Coner('Датчик в точке B')
    coner_2 = Coner('Датчик в точке C')
    print(anemometer_1)
    print(hygrometer_1)
    print(coner_1)
    print(coner_2)
    print('Получаем 10 измерений с датчиков с задержкой в 1 сек')
    for i in range(10):
        anemometer_1.get()
        print(f'{anemometer_1}')
        hygrometer_1.get()
        print(f'{hygrometer_1}')
        coner_1.get()
        coner_2.get()
        print(coner_1)
        print(coner_2)
        time.sleep(1)

    print('Получаем полследние измерения:')
    print(f'Anemometer_1: {anemometer_1.exit}')
    print(f'Hygrometer_1: {hygrometer_1.exit}')
    print(f'Coner_1: {hygrometer_1.exit}')
    print(f'Coner_2: {hygrometer_1.exit}')