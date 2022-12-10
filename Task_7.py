import random
import time
import datetime

class Sensor_value:
    def __init__(self, parameter):
        self.parameter = parameter
        self.date_time = datetime.datetime.now()

    def __str__(self):
        return f'{self.parameter} [{self.date_time}]'

    def __repr__(self):
        return f'({self.parameter} [{self.date_time}])'
    



class Sensor:
    ClassName = "Sensor"
    
    def __str__(self):
        return f'{ self.ClassName }: {self.exit}'

    def get(self):
        pass

class Os_Sensor(Sensor):
    ClassName = "Os_Sensor"
    
    def calibrate(self, min_param, max_param):
        self.min = min_param
        self.max = max_param

    def get(self):
        result = round(self.signal() * (self.max - self.min) + self.min,3)
        self.exit = Sensor_value(result)
        return self.exit

    def signal(self):
        pass

    def __str__(self):
            return f'{ self.ClassName }: {self.exit} max:{self.max}, min: {self.min}'
class HistorySensor(Os_Sensor):
    ClassName = "HistorySensor"
    #время хранения данных указывается в секундах    

    def __init__(self ):
        self.data = []
        
    def get(self):
        super().get()
        self.data.append(self.exit)
        return self.exit

    def __str__(self):
        return super().__str__() + f' GetAll:{self.data}'
        


class Anemometer(HistorySensor):
    ClassName = "Anemometer"

    def signal(self):
        return random.uniform(0, 1)**2

class Hygrometer(HistorySensor):
    ClassName = "Hygrometer"

    def signal(self):
        return random.uniform(0, 1)



anemometer_1 = Anemometer()
hygrometer_1 = Hygrometer()
anemometer_1.calibrate(0,100)
hygrometer_1.calibrate(0,50)
for i in range(10):
    anemometer_1.get()
    hygrometer_1.get()
    time.sleep(1)

print(f'{hygrometer_1}')
print(f'{anemometer_1}')

