#finding the area using Simpson's Rule

import numpy as np
def simpsonsrule(f, xi, xf, n):
   
    if n & 1:
       print ("Error: n is not a even number.")
       return 0.0
    h = float(xf - xi) / n
    integral = 0.0
    x = float(xi)
    for i in range(0, n / 2):
        integral += f(x) + (2.0 * f(x + h))
        x += 2 * h
    integral = (2.0 * integral) - f(xi) + f(xi)
    integral = h * integral / 3.0
    return integral

def f(x): 
    #f(x) = np.cos(x)
    return np.cos(x)
  

xi=0.0; xf=np.pi/2
N = (10,30,100,300,1000)
for n in N:
    print(simpsonsrule(f, xi, xf, n))

#How does the error scale with the number of points?

#>>the error decreases as the number of points increases

##    -Simpson's Rule has much better accuracy than the standard sum we dont need a lots of 
#     points to get the same acuracy in standrad sum as in Simpson's





#Error for SimpsonsRule 

import numpy as np 
from matplotlib import pyplot as plt 
A = (1.0,1.0,1.0,1.0,1.0) # This is exact Aear should be each time
n = (10,30,100,300,1000)  # This is the number of spacings
Axs = (1.05236326978,1.01745333429,1.00523598809,1.00174532926,1.00052359878) # This is the Area using Simpson's Rule
Axi = (1.0764828026941022, 1.025951465275319, 1.0078334198735821, 
1.0026157092462991, 1.0007851925466307) # This is the Area using standard sum
Es = abs(np.subtract(Axs,A))
Ei = abs(np.subtract(Axi,A))

plt.figure()
plt.semilogy(n, Es, 
             color='blue', 
             linewidth = 1.5)
plt.semilogy(n, Ei,
             color= 'red',
             linewidth = 1.5)
plt.title('Semilog y-axis')
plt.grid(True)
plt.show()

