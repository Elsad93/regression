#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


def estimate_coefficients(x,y):
    n= np.size(x)
    mean_x,mean_y= np.mean(x),np.mean(y)
    ss_xy= np.sum(y*x-n*mean_y-y*mean_x)
    ss_xx= np.sum(x*x-n*mean_x-x*mean_x)
    b1= ss_xy/ss_xx
    b0= mean_y-b1*mean_x
    return (b0,b1)

def plot_regression_line(x,y,b):
    plt.scatter(x,y,color='m',marker="o")
    y_pred= b[0]+b[1]*x
    plt.plot(x,y_pred,color='g')
    plt.xlabel('size')
    plt.ylabel('cost')
    plt.show()


# In[7]:


x= np.array([1,2,3,4,5,6,7,8,9,10])
y= np.array([300,350,500,700,800,850,900,900,100,1200])
b= estimate_coefficients(x,y)
print("estimated coefficient: \nb0= {}\nb1={}".format(b[0],b[1]))
plot_regression_line(x,y,b)


# In[ ]:

