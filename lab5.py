import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
fig1=plt.figure()
ax1=fig1.add_subplot()
data=np.loadtxt("load.txt")
x = data[:,0]
y = data[:,1]
f = interp1d(x, y, kind = 'cubic')
xnew = np.linspace(0, 1,33)
ax1.plot(x ,y ,xnew ,f(xnew), '--')
ax1.set_title('1: Сплайн функции')

plt.show()