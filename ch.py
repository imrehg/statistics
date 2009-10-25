import scipy as sp
import scipy.optimize as opt
from scipy.linalg import inv
import pylab as pl

from numpy import loadtxt

data = loadtxt("challenger1.txt")
x = data[:,0]
y = data[:,1]

#def fx(b, x):
#    expo = sp.sum(b * x)
#    return sp.exp(expo) / (1 + sp.exp(expo))
#
#def like(b, x, y):
#    total = 1
#    for i in range(0, len(y)):
#        fi = fx(b, x[i])
##        print 1-y[i]
##        print "test", fi ** y[i], (1-fi) ** (1-y[i])
#        total *= (fi ** y[i]) * ((1-fi) ** (1-y[i]))
#    return sp.log(total)
#
#def difloglike(b, x, y, x0):
#    total = 0
#    for i in range(0, len(y)):
#        total += (y[i] - fx(b, x)) * x[x0]
#    return total
#
#b = []
#diffloglike()

#
#def fx(b, x):
#    expo = sp.sum(b * x)+15
#    return sp.exp(expo) / (1 + sp.exp(expo))
#
#xx = sp.linspace(45, 85)
#b = -0.232
#yy = sp.zeros(len(xx))
#for i in range(0, len(xx)):
#    yy[i] = fx(b, xx[i])
#print yy
#
#pl.plot(x, y,'.')
#pl.plot(xx, yy)
#pl.show()



def response(b, x):
    p = sp.zeros(len(x[:,0]))
    for i in range(0, len(p)):
        xi = sp.matrix(x[i])
        p[i] = 1 / (1 + sp.exp(- sp.sum(sp.multiply(b, xi))))
    return p

def iteration(b, x, y):
    n = len(y)
    p = response(b, x)
    V = sp.zeros((n,n))
    for i in range(0,n):
        V[i,i] = p[i]*(1-p[i])
    vdif = sp.matrix(y - p).T
    V = sp.matrix(V)
    x = sp.matrix(x)
    return inv(x.T * V * x) * x.T * vdif
    
def covm(b, x):
    n = len(x)
    p = response(b, x)
    V = sp.zeros((n,n))
    for i in range(0,n):
        V[i,i] = p[i]*(1-p[i])
    V = sp.matrix(V)
    x = sp.matrix(x)
    return inv(x.T * V * x)

xx = sp.ones((len(x),2))
xx[:,1] = x
b = sp.array([0, 0])

n = 0
while  n < 10:
    bnew = iteration(b, xx, y)
    b =  b + bnew.T
    n += 1
print b
print covm(b, xx)