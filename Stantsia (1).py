#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[51]:


# импорт библиотек
import sys
from solid import *
from solid.utils import * 
# прописываю отдельно каждый элемент
a = translate((0, 0, 0))( 
    cylinder(h = 120, r = 15))

s = mirror((10,0,10))(
    cylinder(h = 60, r = 15))

d = mirror((-10,0,10))(
    cylinder(h = 60, r = 15))
    
f = translate((30, 10, 0))(
    cube([20, 60, 3]))

g = translate( [30, -70, 0])(
    cube( [20, 60, 3]))

h = translate((-50, 10, 0)) (
    cube( [20, 60, 3]))

j = translate((-50, -70, 0)) (
    cube([20, 60, 3]))

k = mirror((-10,0,10))(
    translate(v = [60, 10, 0])( 
    cube(size = [20, 60, 3])))

l = mirror([-10,0,10])(
    translate(v = [60, -70, 0])(
    cube(size = [20, 60, 3])))

z = translate(v = [0, 0, 0])(
    sphere(r=20))

x = mirror([-10,-120,0])(
    translate(v = [0, 0, 120])(
    sphere(r=10)))
                
# соединение всех элементов в 1 объект   

st = a+s+f+d+f+g+h+j+k+l+z+x
# печать кода для 3д моделирования
print(scad_render(st))


# In[ ]:





# In[ ]:




