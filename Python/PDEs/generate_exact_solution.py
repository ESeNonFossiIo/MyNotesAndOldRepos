#!/usr/bin/env python

################################################################################
# Given a potential f and a pressure fild p, this code return an exact solution
# for the Navier Stokes Equations and the relative forcing term.
################################################################################
from sympy import *
import sys

bar="========================================================================"
x,y,t,k = symbols('x y t k')

if len(sys.argv)<3 :
  print bar
  print " Two arguments are required"
  print "  Usage: " + sys.argv[0] + " [forcing term] [pressure]"
  print bar
  exit(0)

# Potential:
f = sys.argv[1]
# Pressure:
p = sys.argv[2]

u=[diff(f,y),-diff(f,x)]
divu=diff(u[0],x)+diff(u[1],y)
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
print " Potential:       " + str(f)
print "========================================================================"
print " Pressure:        " + str(p)
print "========================================================================"
print " div(u):          " + str(divu)
print "========================================================================"
print " grad p:          " + str(gradp)
print "========================================================================"
print " u_t:             " + str(ut)
print "========================================================================"
print " div(grad u):     " + str(lapl)
print "========================================================================"
print " (grad u)u:       " + str(ugradu)
print "========================================================================"
print " Exact solution:  " + str(u)
print "========================================================================"
print " Forcing term:    " + str(forcing)
print "========================================================================"
