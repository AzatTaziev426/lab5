import numpy as np
import matplotlib.pyplot as plt




fig1=plt.figure()

ax1=fig1.add_subplot()

data=np.loadtxt("load.txt")

ax1.plot(data[:,0],data[:,1],':o')
ax1.set_title('1: График функции')

plt.show()