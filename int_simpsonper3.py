from math import sin,pi
import math
N=20
B=1
f = lambda r:((r**2)*(2.718281828**((-3*(r**2))/(2*N*(B**2)))))

a=0
b=1
c=abs(b-a)
h=0.001
n=round((b-a)/h)
S=f(a)+f(b)

for i in 1,2,(n-1):
    S += 4*f(a+(i*h))
for i in 2,2,(n-2):
    S += 2*f(a+i*h)
integral = (h/3) * S
t = ((3/(2*pi*N*B**2))**(3/2))*4*pi*integral
print('hasil= ', t)

exact=f(b)-f(a)
print('exact=', exact)
error=math.fabs(t-exact)
print('error= ', error)
