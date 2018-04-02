from time import sleep
from math import sin
import dynamon

dynamon.path = 'test'

for i in range(50):
    dynamon.push(sin(i/2))
    sleep(0.2)
