################################################################################
# Given a potential f and a pressure fild p, this code return an exact solution
# for the Navier Stokes Equations and the relative forcing term.
################################################################################

from sympy import *

x,y,t,k = symbols('x y t k')

# Potential:
f = t*(x**2)*(y**2)
# Pressure:
p = x*y

u=[diff(f,y),-diff(f,x)]

ut=[diff(u[0],t),diff(u[1],t)]
ugradu=[u[0]*diff(u[0],x)+u[1]*diff(u[0],y) ,
        u[0]*diff(u[1],x)+u[1]*diff(u[1],y) ]
lapl=[diff(u[0],x,2)+diff(u[0],y,2),diff(u[1],x,2)+diff(u[1],y,2) ]
gradp=[diff(p,x),diff(p,y)]

forcing=[ut[i]+ugradu[i]-k*lapl[i]+gradp[i] for i in xrange(2)]

print "========================================================================"
print " Legend: "
print "  - x,y,t = variables "
print "  - k     = viscosity "
print "========================================================================"
print " Exact solution:  " + str(u)
print "========================================================================"
print " Forcing term:    " + str(forcing)
print "========================================================================"
