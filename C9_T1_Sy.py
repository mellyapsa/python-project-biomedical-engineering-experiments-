import math

def integral(t):
    g = 9.8
    m = 78.5
    c = 12.5
    return (g*m/c)*(1-(math.exp(-(c/m)*t)))

def hasil(t):
    g = 9.8
    m = 78.5
    c = 12.5
    return(g*m/c)*(t+((m/c)*math.exp(-(c/m)*t)))

a=0
b=12
h=1

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
exact=fb-fa
error=math.fabs(hasil_integral-exact)

print('integral_simpson1/3 = ', hasil_integral)
print('integral_exact = ', exact)
print('error = ', error)