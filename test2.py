import scipy as sp
from scipy.linalg import inv


def fx(b, x):
    expo = sp.sum(b * x)
    return sp.exp(expo) / (1 + sp.exp(expo))


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

xn = 3
b = sp.array([1, -2, 3, -1.5])
n = 400

# Generate new data
x = sp.ones((n,xn+1))
y = sp.zeros(n)
for i in range(0, n):
    x[i,1:(xn+1)] = sp.random.binomial(1, 0.5, size=(1,xn))
    y[i] = sp.random.binomial(1, fx(b, x[i]))


xx = x
b0 = sp.array([0, 0, 0, 0])
n = 0
while  n < 10:
    bnew = iteration(b, xx, y)
    print bnew.T
    b =  b + bnew.T
    n += 1
print "Result:"
print b
cv = covm(b, xx)
print cv
for i in range(0, xn+1):
    print sp.sqrt(cv[i,i]) * 1.96
