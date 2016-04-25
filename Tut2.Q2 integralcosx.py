Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> np.linspace(0.0, np.pi/2,num=10)
array([ 0.        ,  0.17453293,  0.34906585,  0.52359878,  0.6981317 ,
        0.87266463,  1.04719755,  1.22173048,  1.3962634 ,  1.57079633])
>>> x0=0
>>> x1=np.pi/2
>>> 
>>> dx=0.1
>>> x=np.arange(x0,x1,dx)
>>> y=numpy.sin(x)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    y=numpy.sin(x)
NameError: name 'numpy' is not defined
>>> y=np.sin(x)
>>> tot=y.sum()*dx
>>> print 'integral is' + repr(tot) + 'with dx =' +repr(dx)
integral is0.97836303290220838with dx =0.1
>>> x0=0
>>> ul=[(ul-x0)/10,(ul-x0)/30,(ul-xo)/100,(ul-x0)/300,(ul-x0)/1000]

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ul=[(ul-x0)/10,(ul-x0)/30,(ul-xo)/100,(ul-x0)/300,(ul-x0)/1000]
NameError: name 'ul' is not defined
>>> ul=np.pi/2
>>> delta=[(ul-x0)/10,(ul-x0)/30,(ul-xo)/100,(ul-x0)/300,(ul-x0)/1000]

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    delta=[(ul-x0)/10,(ul-x0)/30,(ul-xo)/100,(ul-x0)/300,(ul-x0)/1000]
NameError: name 'xo' is not defined
>>> x0=0
>>> ul=np.pi/2
>>> delta=[(ul-x0)/10,(ul-x0)/30,(ul-x0)/100,(ul-x0)/300,(ul-x0)/1000]
>>> x=np.arange(x0,ul,dx)
>>> y=np.cos(x)
>>> tot=y.sum()*dx
>>> print 'intergral is ' + repr(tot) + 'with dx=' + repr(dx)
intergral is 1.0502004622913048with dx=0.1
>>> 
