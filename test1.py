import scipy.optimize as opt
import scipy as sp
import pylab as pl

def fx(b, x):
    expo = sp.sum(b * x)
    return sp.exp(expo) / (1 + sp.exp(expo))


def difflike(b, x, y, x0):
    n = len(y)
    total = 0
    for i in range(0, n):
        Fi = fx(b, x[i])
        total += (y[i] - Fi)*x[x0]
    return sp.log(total)


def like(b, x, y):
    total = 1
    for i in range(0, len(y)):
        fi = fx(b, x[i])
#        print 1-y[i]
#        print "test", fi ** y[i], (1-fi) ** (1-y[i])
        total *= (fi ** y[i]) * ((1-fi) ** (1-y[i]))
    return sp.log(total)


def negatlike(b, x, y):
    return -1 * like(b, x, y)


xn = 1
b = sp.array([0, 1])
n = 300

# Generate new data
x = sp.ones((n,xn+1))
y = sp.zeros(n)
for i in range(0, n):
    x[i,1:(xn+1)] = sp.random.binomial(1, 0.5, size=(1,xn))
    y[i] = sp.random.binomial(1, fx(b, x[i]))

#b0 = sp.array([0.05, 0.05, 0.05, 0.05])
#b1, success = opt.leastsq(err, b0, args=(x, y, 3))
#print  b1
#
#print like(b-0.1, x, y)
#print like(b, x, y)
#print like(b+0.1, x, y)
#d = sp.linspace(-0.2,0.2, 21)
#ll = sp.zeros(len(d))
#for di in range(0, len(d)):
#    ll[di] = like(b+d[di], x, y)
#    
#pl.plot(d, ll)
#pl.show()

b0 = sp.array([0, 0])
b1 = opt.fmin(negatlike, b0, args=(x, y))
opt.fmin(
print b1
print negatlike(b, x, y)
