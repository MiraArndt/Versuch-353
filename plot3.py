import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit


x=np.genfromtxt("RCKreis3.csv", delimiter=",",unpack=True,usecols=1)
y=np.genfromtxt("RCKreis3.csv", delimiter=",",unpack=True,usecols=0)

def arctan(x, a, b):
    return a*np.arctan(b*x)

params, covariance_matrix = curve_fit(arctan, x, y, p0=(1, 1))
uncertainties = np.sqrt(np.diag(covariance_matrix))
for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.5f} ± {uncertainty:.5f}')

x_plot = np.linspace(0,10000,10000)

plt.plot(x_plot, (arctan(x_plot, *params)), "-", label='arctan Fit')

plt.legend(loc='best')

plt.plot(x,y,'r.', label = 'Messwerte')
plt.xlabel(r'$t \,/\, \mathrm{ms}$')
plt.ylabel(r'$ln\left(\frac{U_C}{U_0}\right)$')
plt.legend()
plt.xscale('log')

plt.tight_layout()
plt.savefig('plot3.pdf')
