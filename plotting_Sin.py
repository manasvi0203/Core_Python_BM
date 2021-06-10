import numpy as np
import math
import matplotlib.pyplot as plt

# sine curve
x = [0, math.pi/8, math.pi/4, 3*math.pi/8, math.pi/2, 5*math.pi/8, 3*math.pi/4, 7*math.pi/8, math.pi]

y = [np.sin(i) for i in x]

plt.plot(x,y)
plt.show()

import math

import numpy as np
import matplotlib.pyplot as plt
x = [0, math.pi/16,math.pi/14,math.pi/12,math.pi/10,math.pi/8,math.pi/4,3*math.pi/8,math.pi/2,5*math.pi/8,3*math.pi/4,7*math.pi/8,math.pi]

y = [np.cos(i) for i in x]
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
