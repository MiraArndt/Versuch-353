import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = np.linspace(10,10000,100000)


x = ufloat(15058, 0.6)

y = x * 93.2*10**-3
print(y)
#1403.41+/-0.06


#plt.polar(np.arctan(-x), x)

#plt.savefig('polarplot.pdf')