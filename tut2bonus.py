## We obtained the difference of the two Area by integrating the function in to two parts, 
## from -5 to 5. The 1st initial part is from -5 to 3 and 2nd part from 
## 3 to 5, Therefore, we can conclude that the 1st integral is the sum of the two parts and the 2nd integration is
## only for the initial part. 
import numpy
import scipy.integrate as quad
def mygauss(x,cent=0,sig=0.1):
    return numpy.exp(-0.5*(x-cent)**2/sig**2)

I,err=quad.quad(mygauss,-5,5) 
print I
I1,err=quad.quad(mygauss,-5,3)
print I1
I2,err=quad.quad(mygauss, 3,5)
print I2
