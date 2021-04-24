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

faa=integral(a)
fbb=integral(b)

n=0
ganjil=0
genap=0
while a<(b-h):
    a=a+h
    n=n+1
    m=divmod(n,2)
    o=m[1]
    if(o==1):
        fx=integral(a)
        ganjil=ganjil+fx
    else:
        fx = integral(a)
        genap = genap + fx

hasil_integral=h/3*(faa+4*ganjil+2*genap+fbb)
print('integral_simpson1/3 = ', hasil_integral)
