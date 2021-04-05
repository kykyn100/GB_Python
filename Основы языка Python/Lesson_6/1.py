from itertools import cycle
from time import time, sleep


class TrafficLight:

    __color = ('Красный', 'Желтый', 'Зеленый')

    def __init__(self):
        self.timing = cycle([7, 2, 7])
        changer = cycle(TrafficLight.__color)
        while True:
            for mode in self.timing:
                print(next(changer))
                sleep(time() + mode - time())


obj = TrafficLight()



