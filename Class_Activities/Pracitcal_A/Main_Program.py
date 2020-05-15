#Imports
import numpy


class Bus:
    def __init__(self, bus_letter, timing, day, WeekNum):
        self.bus_letter = bus_letter
        self.timing = timing
        self.day = day
        self.WeekNum = WeekNum


bus_1 = Bus("A", "5", "Mon", "2")

print(bus_1.day)