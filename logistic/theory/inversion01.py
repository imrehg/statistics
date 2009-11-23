from sympy.matrices import *
from sympy import *

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = Symbol('e')
f = Symbol('f')
g = Symbol('g')
h = Symbol('h')
i = Symbol('i')
j = Symbol('j')
k = Symbol('k')
l = Symbol('l')

x = Matrix([[a, b, c, d],[b, e, f, g], [c, f, h, i], [d, g, i, j]])
xi = x.inv()
print xi[0,0]
