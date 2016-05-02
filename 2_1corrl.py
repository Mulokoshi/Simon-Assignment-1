##    Tutorial3 Question2a)
##  
from numpy import linspace,arange,real,sin,cos,exp,conj,pi
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt
def corrl(f,g):
    ftf = fft(f)
    cjg = conj(fft(g))
    return ifft(ftf*cjg)

x = linspace(-pi,pi,200)
f = sin(x)
g = exp(-x)
h = corrl(f,g)
h1 = real(h)
plt.plot(x,h1,'b')
plt.title('Correlation of sine and exponential function')
plt.grid(True)
plt.show()
