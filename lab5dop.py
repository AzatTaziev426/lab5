import matplotlib.pyplot as plt
import numpy as np
import math
b=[0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]
o=[0,0.021470,0.293050,0.494105,0.541341,0.516855,0.468617,0.416531,0.367879]
s=0
three=0
trap=0
n=0
a=0
def poly(b,o,t):
    z=0
    for j in range(len(o)):
        p1=1
        p2=1
        for i in range(len(b)):
            if i==j:
                p1=p1*1
                p2=p2*1
            else:
                p1=p1*(t-b[i])
                p2=p2*(b[j]-b[i])
        z=z+o[j]*p1/p2
    return z
newy=[] 
x=np.linspace(np.min(b),np.max(b),100)
y=[poly(b,o,i) for i in x]
for j in range(1,len(x)):
    trap=trap+(poly(b,o,x[j-1])+poly(b,o,x[j]))*(x[j]-x[j-1])/2
    s=s+((poly(b,o,x[j-1])+4*poly(b,o,((x[j-1]+x[j])/2))+poly(b,o,x[j]))*(x[j]-x[j-1])/6)
    three=three+(((poly(b,o,x[j-1]))+3*poly(b,o,((2*x[j-1]+x[j])/3))+3*poly(b,o,((x[j-1]+2*x[j])/3))+poly(b,o,x[j]))*(x[j]-x[j-1]))/8 
n = three - s
a = trap - three
print('Формула Симпсона:',abs(s))
print('Правило Рунге:',abs(three))  
print('Метод трапеций: ',abs(trap))  
print('Погрешность между правилом Рунге и методом Симпсона', n)
print('Погрешность между правилом Рунге и методом Трапеции', a)

plt.plot(b, o, 'o-', x, y)
plt.grid(True)
plt.show()