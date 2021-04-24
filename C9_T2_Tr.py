import math

def integral(z):
    aa = (64*L*miu)/((d**2) * rho)
    return (8*(R**2)/(d**2))*(1/(-aa+math.sqrt((aa**2)+8*g*(z+L))))

L=91.44
miu=0.01
d=0.1
rho=1.0
g=980.0
R=10.0

a=5.0
b=50.0
h=1.0
n=round((b-a)/h)

faa=integral(a)
fbb=integral(b)

jum=0.0
while a<(b-h):
    a = a + h
    fx=integral(a)
    jum=jum+fx

hasil_integral=h/2*(faa+2*jum+fbb)
print('integral_trapezoid = ', hasil_integral)
