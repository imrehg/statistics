import sympy as sy

# Create all symbols used
b1 = sy.Symbol("b1")
b2 = sy.Symbol("b2")
b3 = sy.Symbol("b3")

s1y = sy.Symbol("s1y")
s2y = sy.Symbol("s2y")
s3y = sy.Symbol("s3y")

s1 = sy.Symbol("s1")
s2 = sy.Symbol("s2")
s3 = sy.Symbol("s3")

s12 = sy.Symbol("s12")
s13 = sy.Symbol("s13")
s23 = sy.Symbol("s23")

# Create equation

e1 = b1 * s1**2  - (s1y - b2 * s12 - b3 * s13)
e2 = b2 * s2**2  - (s2y - b1 * s12 - b3 * s23)
e3 = b3 * s3**2  - (s3y - b1 * s13 - b2 * s23)

x = sy.Symbol('x')
y = sy.Symbol('y')

out = sy.solve([sy.Eq(e1, 0), sy.Eq(e2, 0), sy.Eq(e3, 0)], [b1, b2, b3])

xs1y = 9
xs2y = 3
xs3y = 3

xs1 = 3
xs2 = 5
xs3 = 1

xs12 = 2
xs13 = 1
xs23 = 6

print "b1 = ", out[b1]
print "b2 = ", out[b2]
print "b3 = ", out[b3]
xb1 = out[b1].subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
xb2 = out[b2].subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
xb3 = out[b3].subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
print "B1 == ", xb1
print "B2 == ", xb2
print "B3 == ", xb3
xe1 = e1.subs(b1,xb1).subs(b2,xb2).subs(b3,xb3).subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
xe2 = e2.subs(b1,xb1).subs(b2,xb2).subs(b3,xb3).subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
xe3 = e3.subs(b1,xb1).subs(b2,xb2).subs(b3,xb3).subs(s1, xs1).subs(s2,xs2).subs(s3,xs3).subs(s12,xs12).subs(s13,xs13).subs(s23,xs23).subs(s1y,xs1y).subs(s2y,xs2y).subs(s3y,xs3y)
print "E1 == ", xe1
print "E2 == ", xe2
print "E3 == ", xe3