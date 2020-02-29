# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:24:32 2019

@author: belie
"""
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

def get_data_brightness(x):
    filename='./axuv_data/'+str(x)+'.csv'
    csvfile=open(filename,'r',encoding='cp932')
    reader=csv.reader(csvfile,delimiter=',',quotechar='"')
    datalist=[]
    for row in reader:
        datalist.append(row)
    pdlist=pd.DataFrame(datalist)
    axuvdata=pdlist.iloc[47:len(pdlist),:]
    axuvdata.columns=['No','Date','Time','Fine','CH1','CH2','CH3','CH4',
                     'CH5','CH6','CH7','CH8','CH9','CH10','CH11','CH12',
                     'CH13','CH14','CH15','CH16','nan1','nan2','nan3',
                     'nan4','nan5','nan6','nan7','nan8','nan9','nan10',
                     'nan11','nan12']
    axuvdata.index=axuvdata['No']
    del axuvdata['No']
    del axuvdata['Date']
    del axuvdata['Time']
    del axuvdata['nan1']
    del axuvdata['nan2']
    del axuvdata['nan3']
    del axuvdata['nan4']
    del axuvdata['nan5']
    del axuvdata['nan6']
    del axuvdata['nan7']
    del axuvdata['nan8']
    del axuvdata['nan9']
    del axuvdata['nan10']
    del axuvdata['nan11']
    del axuvdata['nan12']

    space=(int(axuvdata['Fine'][1])-int(axuvdata['Fine'][0]))
    axuvtime=np.linspace(0,space*len(axuvdata)*10**(-6),len(axuvdata),dtype=float)
    
    del axuvdata['Fine']
    
    
    #Read setting value
    pdlist=pd.DataFrame(datalist)
    axuvsetting=pdlist.iloc[17:33,:]
    axuvsetting.columns=['No','CH','HSV','Mode','Range','Filter','Max','Min',
                         'Unit','Color','Color1','Color2','Zero','nan14','nan15',
                         'nan16','nan17','nan18','nan19','nan20','nan1','nan2',
                         'nan3','nan4','nan5','nan6','nan7','nan8','nan9','nan10','nan11','nan12']
    axuvsetting=axuvsetting.reset_index()
    
    #Solve saturation
    for i in range(0,len(axuvdata.iloc[0,:])-1):
        #axuv_down_limit=axuvdata.iloc[:,i][axuvdata.iloc[:,i]==str('-------')]
        #axuv_up_limit=axuvdata.iloc[:,i][axuvdata.iloc[:,i]==str('+++++++')]
        #print(axuv_down_limit)
        #print(axuv_up_limit)
        (axuvdata.iloc[:,i][axuvdata.iloc[:,i]==str('+++++++')])=float(axuvsetting['Max'][i])*2*1.1
        (axuvdata.iloc[:,i][axuvdata.iloc[:,i]==str('-------')])=-float(axuvsetting['Max'][i])*2*1.1
    
    #Change Read data type from object to float

    axuvdata=axuvdata.astype('float')
    
    #Substract offset from axuv data
    offsetnew=[]
    for i in range(0,len(axuvdata.iloc[0,:])):
        offsetnew.append(np.average(axuvdata.iloc[0:100,i]))
    npoffset=offsetnew
    npaxuvdata=axuvdata.values
    nplowaxuv=npaxuvdata-npoffset
    
    #Read Etendu value
    filename_etendu='./axuv_data/Etendu_volume_new.csv'
    lowetendu=pd.read_csv(filename_etendu,
                          encoding='utf_8',
                          skiprows=None,
                          header=None,
                          index_col=None,
                          names=['Nan','etendu'],
                          delimiter=',')
    del lowetendu['Nan']
    etendu=lowetendu.transpose()
    npetendu=etendu.values
    
    #Calculation Brightness
    nplowbright=np.divide(nplowaxuv,npetendu)
    #Unit [mV/(mm^2*radian)]=>[W/m^2]
    #[mV]=>[V],Resistance 100kΩ, Efficiency 0.24[W/A],4Π[radian], [mm^2]=>[m^2]
    #npbright=nplowbright*10**(-3)/(10**5)/0.24*4*np.pi*(10**6)
    #[V]=>[V],Resistance 100kΩ, Efficiency 0.24[W/A],4Π[radian], [mm^2]=>[m^2]
    npbright=nplowbright/(10**5)/0.24*4*np.pi*(10**6)
    brightness=pd.DataFrame(npbright,
                            columns=['Halpha','CH2','CH3','CH4',
                                     'CH5','CH6','CH7','CH8',
                                     'CH9','CH10','CH11','CH12',
                                     'CH13','CH14','CH15','CH16'])
    brightness['time']=list(axuvtime)
    print('Complete translation to brightness')
    return brightness

shot_number=40416
axuv=get_data_brightness(shot_number)

axuv_array_ch8=np.array([axuv['time'].values,-axuv['Halpha'],axuv['CH8']])
axuv_csv_ch8=pd.DataFrame(transpose(axuv_array_ch8),columns=['time','Halpha','CH8'])
#print(axuv_low)


    # to make new file
if not os.path.exists('./csv_data_28GHz'):
    os.mkdir('./csv_data_28GHz')
"""
if not os.path.exists('./csv_data_28GHz/%s'%(shot_num)):
    os.mkdir('./csv_data_28GHz/%s'%(shot_num))
"""
if not os.path.exists('./csv_data_28GHz/axuv'):
    os.mkdir('./csv_data_28GHz/axuv')
csv_name='./csv_data_28GHz/axuv/%s_axuv.txt'%(shot_number)
axuv.to_csv(csv_name,encoding='utf_8',index=None,sep=",")
csv_ch8_name='./csv_data_28GHz/axuv/%s_axuv_ch8_tab.txt'%(shot_number)
axuv_csv_ch8.to_csv(csv_ch8_name,encoding='utf_8',index=None,sep=",")



print(axuv)

#%%
plt.figure()
axs=plt.subplot(2,1,1)
axs.plot(axuv['time'],-axuv['Halpha'])
axs1=plt.subplot(2,1,2)
axs1.plot(axuv['time'],axuv['CH8'])
plt.show()

#%%
filename_etendu='./axuv_data/Etendu_volume_new.csv'
lowetendu=pd.read_csv(filename_etendu,
                          encoding='utf_8',
                          skiprows=None,
                          header=None,
                          index_col=None,
                          names=['Nan','etendu'],
                          delimiter=',')
