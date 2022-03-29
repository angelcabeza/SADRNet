#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:50:42 2022

@author: angel
"""


#%% DEFINES BLOCKS OF CODE
import numpy as np # math library
import scipy # scientific library
import pylab as pl # plotting library
#%% this will output some wisdom
print('Python and Calcium Imaging, a marriage made in heaven')
#%% this creates a random vector
a = np.random.random([10,10])
print(a)
#%% this will plot something
pl.imshow(a)