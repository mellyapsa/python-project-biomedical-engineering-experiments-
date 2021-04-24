#dwi melly aprilia sari / 081811733027 / B6
import math

def integral(x):
    return math.sin(x)

def hasil(x):
    return math.cos(x)

pi=22/7
a=0
b=pi/4
h=pi/6

fa=hasil(a)
fb=hasil(b)
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
exact=math.fabs(fb-fa)
error=math.fabs(hasil_integral-exact)

print('massa total pelat tipis seragam dengan simpson 1/3= ', hasil_integral)
print('masa total pelat tipis exact = ', exact)
print('error = ', error)