import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit

x=np.genfromtxt("RCKreis2.csv", delimiter=",",unpack=True,usecols=1)
y=np.genfromtxt("RCKreis2.csv", delimiter=",",unpack=True,usecols=0)

#def exp(x, a, b):
   # return np.exp(-a*x+b)
#params, covariance_matrix = curve_fit(exp, x, y, p0=(-0.0002, 1))


def exp(x, a, b):
    return a/(np.sqrt(1+(x/2*np.pi)**2*b**2))

params, covariance_matrix = curve_fit(exp, x, y, p0=(1, 0.004))


uncertainties = np.sqrt(np.diag(covariance_matrix))
for name, value, uncertainty in zip('ab', params, uncertainties): 
    print(f'{name} = {value:8.5f} ± {uncertainty:.5f}')

a = np.linspace(10,10000,10000)

w = 1.40341
f = w/(2*np.pi)

#(np.sqrt(1+(x_plot)^2*(1.40341)**2))**(-1)

plt.plot(a, (np.sqrt(1+(f*a)**2))**(-1) , "-", label='A(\nu_i)/U_0')

plt.legend(loc='best')

plt.plot(x,y,'r.', label = 'Messwerte')
plt.xlabel(r'$t \,/\, \mathrm{ms}$')
plt.ylabel(r'$ln\left(\frac{U_C}{U_0}\right)$')
plt.legend()
plt.xscale('log')



plt.tight_layout()
plt.savefig('plot2.pdf')
