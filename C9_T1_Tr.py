import math

def integral(t):
    return (g*m/c)*(1-(math.exp(-(c/m)*t)))

#def hasil(t):
    return(g*m/c)*(t+((m/c)*math.exp(-(c/m)*t)))

g = 9.8
m = 78.5
c = 12.5

a=0
b=12
h=1
n=round((b-a)/h)

#fa=hasil(a)
#fb=hasil(b)
faa=integral(a)
fbb=integral(b)

jum=0
while a<(b-h):
    a = a + h
    fx=integral(a)
    jum=jum+fx

hasil_integral=h/2*(faa+2*jum+fbb)
#exact=quad(integral(a,b))
#error=math.fabs(hasil_integral-exact)

print('integral_trapezoid = ', hasil_integral)
#print('integral_exact = ', exact)
#print('error = ', error)