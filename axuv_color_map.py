#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reset', '-f')


# In[2]:


import pandas as pd
import urllib.request
import math
import datetime
import numpy as np
from numpy import *
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *
import time
import scipy as sc
import csv
import os
import axuv_graphtec as tec


# In[3]:


shot_num=38103
downconvert=100
axuv=tec.get_data_axuv_graphtec(shot_num)
axuv_brightness=tec.get_data_brightness_graphtec(shot_num)


# In[4]:


# to make new file
if not os.path.exists('./figure_data_axuv'):
    os.mkdir('./figure_data_axuv')
if not os.path.exists('./figure_data_axuv/color_map'):
    os.mkdir('./figure_data_axuv/color_map')
if not os.path.exists('./figure_data_axuv/color_map/%s'%(shot_num)):
    os.mkdir('./figure_data_axuv/color_map/%s'%(shot_num))
file_name_fig='./figure_data_axuv/color_map/%s/'%(shot_num)       


# In[5]:


axuv


# In[6]:


axuv_brightness[0:5]


# In[7]:


plt.plot(axuv_brightness['time'],axuv_brightness['CH5'])
plt.show()


# In[8]:


axuv_brightness['CH5']=(axuv_brightness['CH4']+axuv_brightness['CH3'])/2


# In[9]:


plt.plot(axuv_brightness['time'],axuv_brightness['CH5'])
plt.show()


# In[10]:


plt.plot(axuv_brightness['time'],axuv_brightness['CH8'])
plt.xlim(0.01,0.024)
plt.show()


# In[11]:


axuv_brightness


# In[12]:


plt.rcParams['lines.linewidth'] = 0.001


# In[13]:


import numpy as np
from matplotlib import colors, ticker, cm
origin = 'lower'

# 滑らかな塗りつぶし
X=np.linspace(min(axuv_brightness['time']), max(axuv_brightness['time']), len(axuv))
#Y=np.linspace(1.5, 16.5, 16)
Y=np.array([716.79,644.58,554.33,443.47,311.42,161.21,0.30013,-160.63,
            -310.9,-443.02,-553.96,-644.28,-716.55,-773.96,-819.54])
X2,Y2=np.meshgrid(X,Y)

zaxis=axuv_brightness
zaxis1=zaxis.drop('time', axis=1)
zaxis2=zaxis1.drop('CH1', axis=1)
Z = zaxis2.values
#current=get_data_current(shot_num)



fig, axs = plt.subplots(1, 1, sharex=True,figsize=(10, 5));
    # Remove horizontal space between axes
fig.subplots_adjust(hspace=0.15)





cs = axs.contourf(X, Y/1000, transpose(Z), 30, cmap=plt.cm.plasma,origin=origin)
CS2 = plt.contour(cs, levels=cs.levels[::1],
                  colors='w',
                  origin=origin)


# Make a colorbar for the ContourSet returned by the contourf call.
cbar = plt.colorbar(cs)
cbar.ax.set_ylabel('Brightness [W/m$^2$]')
# Add the contour line levels to the colorbar
cbar.add_lines(CS2)


axs.set_ylabel('Tangential radius [m]')
axs.set_xlabel('Time (sec)' )
axs.set_yticks(np.arange(-1, 1, 0.2))
#axs.set_yticks(np.arange(0, 20, 1))
#axs.set_xlim(low_time, high_time)
axs.set_xlim(0.019, 0.023)
axs.set_ylim(-0.7,0.7)
#axs.set_ylim(1.5,16.5)
axs.grid(linestyle=':')

plt.show()


fig_name_column=file_name_fig+'impact_short_after_%s'%(shot_num)
fig.savefig(fig_name_column,bbox_inches="tight")
fig_name_column=file_name_fig+'impact_short_after_%s.svg'%(shot_num)
fig.savefig(fig_name_column,bbox_inches="tight")


# In[14]:


fig_share_name='/Volumes/share/axuv_chi/figure/'
fig_name_column=fig_share_name+'impact_short_after_%s'%(shot_num)
fig.savefig(fig_name_column,bbox_inches="tight")
fig_name_column=fig_share_name+'impact_short_after_%s.svg'%(shot_num)
fig.savefig(fig_name_column,bbox_inches="tight")

csv_name='/Volumes/share/axuv_chi/data/axuv_%s.csv'%(shot_num)
axuv_brightness.to_csv(csv_name,encoding='utf_8',index=None,sep=",")
csv_name_txt='/Volumes/share/axuv_chi/data/axuv_%s.txt'%(shot_num)
axuv_brightness.to_csv(csv_name_txt,encoding='utf_8',index=None,sep=",")


# In[15]:


axuv_numpy=axuv_brightness.values


# In[16]:


axuv_numpy


# #### 
