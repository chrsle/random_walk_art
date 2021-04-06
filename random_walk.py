#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy
import pylab
import random


# In[16]:


for a in numpy.arange(101):
    print(a)
    n = 29200
    x = numpy.zeros(n)
    y = numpy.zeros(n)
    for i in range(1, n):
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1

    pylab.title(str(a))
    pylab.plot(x, y)
    pylab.axis('off')
    pylab.savefig(str(a)+".png",bbox_inches="tight",dpi=600)
    pylab.show()


# In[ ]:




