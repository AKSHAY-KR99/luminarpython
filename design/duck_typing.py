class Swift:
    def drive(self):
        print("Driving SWift Car")

class Roylce_royce:
    def drive(self):
        print("Driving RR ")
class Ferarri:
    def drive(self):
        print("driving Ferarrii")

class Person:
    def start(self,car):
        car.drive()

sw=Swift()
p=Person()
p.start(sw)

rr=Roylce_royce()
p=Person()
p.start(rr)

fer=Ferarri()
p=Person()
p.start(fer)

import threading
print(threading.currentThread().getName())