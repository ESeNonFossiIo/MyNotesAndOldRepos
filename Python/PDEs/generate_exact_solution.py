from sympy import *

x,y,t,k = symbols('x y t k')

f = (x**2)*(y**2)
p = x*y

u=[diff(f,y),-diff(f,x)]

ugradu=[u[0]*diff(u[0],x)+u[1]*diff(u[0],y) ,
        u[0]*diff(u[1],x)+u[1]*diff(u[1],y) ]

lapl=[diff(u[0],x,2)+diff(u[0],y,2),diff(u[1],x,2)+diff(u[1],y,2) ]

gradp=[diff(p,x),diff(p,y)]

print ugradu
print lapl

result=[ugradu[i]-k*lapl[i]+gradp[i] for i in xrange(2)]
print result

