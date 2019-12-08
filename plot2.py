import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit


x=np.genfromtxt("RCKreis2.csv", delimiter=",",unpack=True,usecols=1)
y=np.genfromtxt("RCKreis2.csv", delimiter=",",unpack=True,usecols=0)


def sigmoid(x, a, b, c, d):
    return a / (1 + np.exp(-(d*x - b))) + c

params, covariance_matrix = curve_fit(sigmoid, x, y, p0=(-6, 1.6, 6, 0.1))
uncertainties = np.sqrt(np.diag(covariance_matrix))
for name, value, uncertainty in zip('abcd', params, uncertainties): 
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')

x_plot = np.linspace(0,10000,10000)


plt.plot(x_plot, np.log(sigmoid(x_plot, *params)), "-", label='Sigmoid Fit')

plt.legend(loc='best')

plt.plot(x,y,'r.', label = 'Messwerte')
plt.xlabel(r'$t \,/\, \mathrm{ms}$')
plt.ylabel(r'$ln\left(\frac{U_C}{U_0}\right)$')
plt.legend()
plt.xscale('log')



plt.tight_layout()
plt.savefig('plot2.pdf')
