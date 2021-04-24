import math

NN=20
b=1
def fungsi(r):
    return (pow((3/(2*3.14*NN*b*b)),(3/2)))*(math.exp((-3*r*r)/(2*NN*b*b))*4*3.14*r*r)
a=0
b=1
N=2
h=(b-a)/N
fa=fungsi(a)
fb=fungsi(b)
jum=0
for i in range (1,N):
    a=a+h
    jum=jum+fungsi(a)
hasil_integ=h/2*(fa+2*jum+fb)
print('hasil trapezoid 4 segmen=',hasil_integ)
