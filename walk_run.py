import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from walk_func import walk_cauchy, walk_gauss

N = 500 #number of steps


#################### GAUSSIAN ####################

##### plotting trajectory #####
x1, y1 = walk_gauss(N)[0], walk_gauss(N)[1]

plt.plot(x1[0],y1[0],'go')
plt.plot(x1[-1],y1[-1],'ro')
plt.legend(['start','finish'])
plt.plot(x1,y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Walk for {} steps'.format(N))
plt.show()

##### simulating average distance #####
YS1 = []
Y1 = []
for j in range(0,310,10):
    for i in range(200):
        Y1.append(walk_gauss(j)[2])
    YS1.append(np.mean(Y1))

XS1 = np.linspace(0,300,31)

plt.plot(XS1,YS1,'o')
plt.xlabel('number of steps')
plt.ylabel('average distance')
plt.show()


def f(x,a,b,c):
    return a + b * np.sqrt(x + c)

popt, pcov = curve_fit(f,XS1,YS1)
popt


domain1 = np.linspace(0,300,1000)

plt.plot(XS1,YS1,'o')
plt.plot(domain1, f(domain1,*popt), 'r')
plt.xlabel('number of steps')
plt.ylabel('average distance')
plt.legend(['points','fitted curve'])
plt.show()
#################### GAUSSIAN ####################



#################### CAUCHY ####################

##### plotting trajectory #####
x2, y2 = walk_cauchy(N)[0], walk_cauchy(N)[1]

plt.plot(x2[0],y2[0],'go')
plt.plot(x2[-1],y2[-1],'ro')
plt.legend(['start','finish'])
plt.plot(x2,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Walk for {} steps'.format(N))
plt.show()

##### simulating average distance #####
YS2 = []
Y2 = []
for j in range(0,310,10):
    for i in range(200):
        Y2.append(walk_cauchy(j)[2])
    YS2.append(np.mean(Y2))

XS2 = np.linspace(0,300,31)

plt.plot(XS2,YS2,'o')
plt.xlabel('number of steps')
plt.ylabel('average distance')
plt.show()

def g(x,a,b):
    return a*x+b

popt2, pcov2 = curve_fit(g,XS2,YS2)
popt2


plt.plot(XS2,YS2,'o')
plt.plot(domain1, g(domain1,*popt2), 'r')
plt.xlabel('number of steps')
plt.ylabel('average distance')
plt.legend(['points','fitted curve'])
plt.show()
#################### CAUCHY ####################
