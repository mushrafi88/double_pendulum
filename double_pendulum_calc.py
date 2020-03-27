#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m1  = 1.0              
m2  = 1.0
l1  = 10.0             
l2  = 10.0
g   = 9.81              
dt  = 0.01            
M   = m2 / (m1+m2) 
l   = l1/l2    
dx  = dt/5
R   = 1                    #radius of bob
r   = 0.1
pi  = 3.141592653589793238


# In[2]:


from math import * 
from numpy import*


# In[3]:


def alpha1(ang_1, ang_2):
    return (1/l)*M*cos(ang_1-ang_2)
def alpha2(ang_1, ang_2):
    return l*cos(ang_1-ang_2)
def f1(ang_1, ang_2, w1, w2):
    return (-1/l)*M*(w2**2)*sin(ang_1-ang_2)-(g/l1)*sin(ang_1)
def f2(ang_1, ang_2, w1, w2):
    return l*(w1**2)*sin(ang_1-ang_2)-(g/l2)*sin(ang_2)

def g1(ang_1, ang_2, w1, w2):
    return w1      
def g2(ang_1, ang_2, w1, w2):
    return w2   
def g3(ang_1, ang_2, w1, w2):
    return (f1(ang_1, ang_2, w1, w2)-alpha1(ang_1, ang_2)*f2(ang_1, ang_2, w1, w2))/(1-alpha1(ang_1, ang_2)*alpha2(ang_1, ang_2))
def g4(ang_1, ang_2, w1, w2):
    return (f2(ang_1, ang_2, w1, w2)-f1(ang_1, ang_2, w1, w2)*alpha2(ang_1, ang_2))/(1-alpha1(ang_1, ang_2)*alpha2(ang_1, ang_2))
   


# In[4]:


# Initial Value
x1 = pi/2         # theta1
x2 = pi/2         # theta2
x3 = 0.0              # w1i
x4 = 0.0              # w2i
t  = 0.0              # time
y1 = [x1]
y2 = [x2]
y3 = [x3]
y4 = [x4]


# In[5]:


for x in range(1,100000):
    # Calculate using Runge-Kutta 4th
        t = t + dt
        k11 = g1(x1, x2, x3, x4)
        k12 = g2(x1, x2, x3, x4)
        k13 = g3(x1, x2, x3, x4)
        k14 = g4(x1, x2, x3, x4)
        k21 = g1(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k22 = g2(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k23 = g3(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k24 = g4(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k31 = g1(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k32 = g2(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k33 = g3(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k34 = g4(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k41 = g1(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k42 = g2(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k43 = g3(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k44 = g4(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        
        # Update angle and angular velocity
        x1 = x1 + dx * (k11 + 2*k21 + 2*k31 + k41)
        y1.append(x1)
        x2 = x2 + dx * (k12 + 2*k22 + 2*k32 + k42)
        y2.append(x2)
        x3 = x3 + dx * (k13 + 2*k23 + 2*k33 + k43)
        y3.append(x3)
        x4 = x4 + dx * (k14 + 2*k24 + 2*k34 + k44)
        y4.append(x4)


# In[6]:


zip(y1,y2,y3,y4)


# In[7]:


import csv
with open('double_pend.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(y1,y2,y3,y4))
quit()    


# In[1]:



cat double_pend.csv

