import matplotlib.pyplot as plt
import numpy as np
import csv

x=np.genfromtxt("RCKreis.csv", delimiter=",",unpack=True,usecols=0)
y=np.genfromtxt("RCKreis.csv", delimiter=",",unpack=True,usecols=1)

params, covariance_matrix = np.polyfit(x, np.log(y), deg=1, cov=True)
x_plot = np.linspace(0,3,100)

print(params[1])

print(params[0])


plt.plot(
   x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.plot(x,np.log(y),'r.', label = 'Messwerte')
plt.xlabel(r'$t \,/\, \mathrm{ms}$')
plt.ylabel(r'$ln\left(\frac{U_C}{U_0}\right)$')
plt.legend()



plt.tight_layout()
plt.savefig('plot.pdf')
