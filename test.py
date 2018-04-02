from time import sleep
from math import sin, cos
import dynamon

# See output at https://dynamon.io/test
dynamon.path = 'test'

dynamon.clear()

for i in range(50):
    theta = i/2
    dynamon.push(i, [sin(theta), cos(theta)])
    sleep(0.2)
