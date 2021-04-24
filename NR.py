import math

def f(x):
    return (a**x)-(3*x**2)+(3*x)

def f1(x):
    return (a**x)*(-9.210340372)-(2*3*x)+3
x=50
a=0.0001
max=10 #maksimal iterasi
for i in range (1,max+1):
  x=x-(f(x)/f1(x))
  error=math.fabs(f(x))
  print('i = ', i, '| x = ',x, '| error = ',error)