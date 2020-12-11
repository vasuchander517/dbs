#!/usr/bin/env python
# coding: utf-8

# In[79]:


import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[60]:


def f(x,y):
    if x > 0:
        x_value = math.exp(-x-y)
    else:
        x_value = 0
    if y > 0:
        y_value = math.exp(-x-y)
    else:
        y_value = 0
    return x_value,y_value    
    


# In[81]:


size = 100
x = np.random.randn(size)
y = np.random.randn(size)

for i in range(size):
    x[i],y[i] = f(x[i],y[i])


# In[97]:


sns.jointplot(x,y,kind='reg')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[ ]:




