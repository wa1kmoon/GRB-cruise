# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:16:57 2019

@author: Vanistar
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci

file = './measurements.csv'
datafile=open(file,'r')

z = 0.4745
#cosmological parameters
H0=67.3 #km/s/Mpc
Oa = 0.685
Om = 0.315
c = 2.99e5 # km/s

def dl(z):
    return ((1+z)**2 * (1+Om*z)-z*(2+z)*Oa)**(-1/2)

sci.romberg(dl,0,z)
miu = 5 * np.log10(sci.romberg(dl,0,z)*c*(1+z)*10**5/H0)

#apparent mag to absolute mag
def ap2ab(m,miu):
    return m-miu
#observer time to rest frame time
def ot2rt(t,z):
    return t/(1+z)

Rmag=[]
time=[]
Rerr=[]

for item in datafile.readlines():
    t,m,e=map(float, item.strip('\n').split(','))
    Rmag.append(m)
    time.append(t)
    Rerr.append(e)


#rot = np.array(rtime)
#rt = ot2rt(rot,z)
Rt = np.array(time)
Re = np.array(Rerr)  
Rm = np.array(Rmag)

fig, ax = plt.subplots(figsize=(14,8))
ax.plot(Rt,Rm,'r.')
ax.set_xscale("log")
ax.errorbar(Rt,Rm,yerr=Re,fmt='.r')
ax.set_ylim(22,19.0)