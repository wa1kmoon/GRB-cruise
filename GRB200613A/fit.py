# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:23:45 2019

@author: Vanistar
"""
from readdata import*
from functions import* 
import emcee
import numpy as np
import corner
import matplotlib.pyplot as plt
import scipy.integrate as sci

# fit afterglow of GRB 
def lnlike(theta,x,y,yerr):
    a1,a2,tb,B=theta
    model = -2.5*np.log10(((x/tb)**a1+(x/tb)**a2)**-1)+B
    inv_sigma2 = 1.0/yerr**2
    return -0.5*(np.sum((y-model)**2*inv_sigma2))

def lnprior(theta):
    a1, a2, tb, B=theta
    if 0.0 < a1 < 5.0 and 0.0 < a2 < 5.0 and 0.0 < tb < 5.0:
        return 0.0
    return -np.inf

def lnprob(theta, x, y, yerr):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(theta, x, y, yerr)

ndim, nwalkers = 4, 100
pos_min = np.array([0.0, 0.0, 0, -10])
pos_max = np.array([3.0, 3.0, 5, 100])
pos_int = pos_max - pos_min
pos = [pos_min + pos_int*np.random.rand(ndim) for i in range(nwalkers)]  

d = 6

Rmg = Rm[:d]
Rtg = Rt[:d]
Reg = Re[:d]
x, y, yerr = Rtg,Rmg,Reg
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))

sampler.run_mcmc(pos, 500)
samples = sampler.chain[:, 50:, :].reshape((-1, ndim))


fig = corner.corner(samples, labels=["$α1$","$α2$","$Tb$","$B$"])
fig.savefig("contour.png")

a1, a2, tb, B = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
							zip(*np.percentile(samples, [16, 50, 84],
												axis=0)))
print("a1:{}\na2:{}\ntb:{}\nB:{}".format(a1,a2,tb,B))

with open('fit.txt','w') as fitfile:
    fitfile.write("a1:{}\na2:{}\ntb:{}\nB:{}".format(a1,a2,tb,B))

xp = np.arange(0,10,0.01)
fig, ax = plt.subplots()
ax.set_xscale('log')
#ax.plot(Rtg,Rmg,'r.')
ax.plot(xp,blk(a1[0],a2[0],tb[0],B[0],xp),'k')
ax.errorbar(Rt,Rm,yerr=Re,fmt='.r')
ax.set_xlim(0.1,10)
ax.set_ylim(22,14)
plt.xlabel('time since burst (day)')
plt.ylabel('M (mag)')
plt.savefig('lightcurve.png',dpi=1000)

#GRB 余辉去除
# rfg = fluxfrac(blk(a1[0],a2[0],tb[0],B[0],rt[d:]))
# rfs = fluxfrac(rm[d:])
# rm_gsub = flux2mag(rfs-rfg)
# rmab = rm_gsub-miu

# dict = {}
# for item in range(len(rmab)):
#     dict[rt[d+item]]=rmab[item]

#SN 拟合
# rmp = np.poly1d(np.polyfit(rt[d:],rmab,5))
# rmab_min = min(rmp(xp)[:3000])
# rindex = list(rmp(xp)).index(rmab_min)
# rt_min = xp[rindex]
# rmab_15 = rmp(xp[rindex+1500])
# r_delta = rmab_15 - rmab_min
# print("peak:{:.2f},delta:{:.2f},peaktime:{:.2f}".format(rmab_min,r_delta,rt_min))
#plt.figure(figsize=(7,4))
#plt.plot(rt[d:],rmab,'r.')
#plt.errorbar(rt[d:],rmab,yerr=re[d:],fmt='.r')
#plt.plot(xp,rmp(xp),'k')
#plt.xlim(0,40)
#plt.ylim(-14,-20)
#plt.xlabel("time since burst (day)")
#plt.ylabel('M (AB mag)')
#plt.text(40*0.64,-14-6*0.9,'rest frame r band', style = 'italic',bbox = {'facecolor':'white'})
#plt.savefig('rsn.png',dpi=1000)
