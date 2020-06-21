# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:08:15 2019

@author: Vanistar
"""

import numpy as np

br = 1.2e-10

def blk(a1,a2,tb,B,x):
    return -2.5*np.log10(((x/tb)**a1+(x/tb)**a2)**-1)+B

def spl(a1,B,x):
    return -2.5*(-a1)*np.log10(x)+B

def fluxfrac(m):
    global br
    return 2*br*np.sinh((-m*np.log(10)/2.5) - np.log(br))

def flux2mag(f):
    global br
    return (-2.5/np.log(10)) * (np.arcsinh(f/(2*br)) + np.log(br))

def Jf2m(f):
    return -2.5*np.log10(f)

def Jm2f(m):
    return np.power(10,m/(-2.5))

#BKK FIT
def blnlike(theta,x,y,yerr):
    a1,a2,tb,B=theta
    model = -2.5*np.log10(((x/tb)**a1+(x/tb)**a2)**-1)+B
    inv_sigma2 = 1.0/yerr**2
    return -0.5*(np.sum((y-model)**2*inv_sigma2))

def blnprior(theta):
    a1, a2, tb, B=theta
    if 0.0 < a1 < 2.0 and 0.0 < a2 < 2.0 and 0.0 < tb < 1.0:
        return 0.0
    return -np.inf

def blnprob(theta, x, y, yerr):
    lp = blnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + blnlike(theta, x, y, yerr)

#ndim, nwalkers = 4, 100
#pos_min = np.array([0.0, 1.0, 0, -10])
#pos_max = np.array([1.0, 2.0, 2, 20])
#pos_int = pos_max - pos_min
#pos = [pos_min + pos_int*np.random.rand(ndim) for i in range(nwalkers)]  
#
#d = 7
#
#rmg = rm_hsub[:d]
#rtg = rt[:d]
#reg = re[:d]
#x, y, yerr = rtg,rmg,reg
#sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))
#
#sampler.run_mcmc(pos, 500)
#samples = sampler.chain[:, 50:, :].reshape((-1, ndim))


#fig = corner.corner(samples, labels=["$α1$","$α2$","$Tb$","$B$"])
#fig.savefig("triangle.png")

#a1, a2, tb, B = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
#							zip(*np.percentile(samples, [16, 50, 84],
#												axis=0)))
#print("a1:{}\na2:{}\ntb:{}\nB:{}".format(a1,a2,tb,B))


#SPL FIT
def slnlike(theta,x,y,yerr):
    a1,B=theta
    model = 2.5*a1*np.log10(x)+B
    inv_sigma2 = 1.0/yerr**2
    return -0.5*(np.sum((y-model)**2*inv_sigma2))

def slnprior(theta):
    a1, B=theta
    if 0.0 < a1 < 2.0:
        return 0.0
    return -np.inf

def slnprob(theta, x, y, yerr):
    lp = slnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + slnlike(theta, x, y, yerr)

#ndim, nwalkers = 2, 100
#pos_min = np.array([0.0, 0])
#pos_max = np.array([2.0, 30])
#pos_int = pos_max - pos_min
#pos = [pos_min + pos_int*np.random.rand(ndim) for i in range(nwalkers)]  
#d = 7
#Rtg = Rt[:d] 
#Rmg = Rm_hsub[:d]
#Reg = Re[:d]
#
#x, y, yerr = Rtg,Rmg,Reg
#sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))
#
#sampler.run_mcmc(pos, 500)
#samples = sampler.chain[:, 50:, :].reshape((-1, ndim))

#fig = corner.corner(samples, labels=["$α1$","$B$"])
#fig.savefig("triangle.png")

#a1,B = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]),
#							zip(*np.percentile(samples, [16, 50, 84],
#												axis=0)))
#print("a1:{}\nB:{}".format(a1_mcmc,B_mcmc))
