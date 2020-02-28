
# coding: utf-8

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


# In[3]:

def get_data_axuv_82(shotnumber,**kws):
    #filename='./axuv_data/AXUV_'+str(x)+'.csv'
    basedir = kws.get('basedir','../data')
    # TODO: add function to scan datafolder (copy from my SIF reader)
    filename = f'{basedir}/AXUV_{shotnumber}.csv'

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
                     'nan11','nan12','nan13']
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
    del axuvdata['nan13']
    space=(int(axuvdata['Fine'][1])-int(axuvdata['Fine'][0]))
    axuvtime=np.linspace(0,space*len(axuvdata)*10**(-6),len(axuvdata),dtype=float)
    axuvdata['time']=list(axuvtime)
    del axuvdata['Fine']
    return axuvdata


# In[140]:

def get_data_brightness_82(x):
    filename='./axuv_data/AXUV_'+str(x)+'.csv'
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
                     'nan11','nan12','nan13']
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
    del axuvdata['nan13']
    space=(int(axuvdata['Fine'][1])-int(axuvdata['Fine'][0]))
    axuvtime=np.linspace(0,space*len(axuvdata)*10**(-6),len(axuvdata),dtype=float)
    
    del axuvdata['Fine']
    
    
    #Read setting value
    pdlist=pd.DataFrame(datalist)
    axuvsetting=pdlist.iloc[17:33,:]
    axuvsetting.columns=['No','CH','HSV','Mode','Range','Filter','Max','Min',
                         'Unit','Color','Color1','Color2','Zero','nan14','nan15',
                         'nan16','nan17','nan18','nan19','nan20','nan1','nan2',
                         'nan3','nan4','nan5','nan6','nan7','nan8','nan9','nan10','nan11','nan12','nan13']
    axuvsetting=axuvsetting.reset_index()
    
    #Solve sachireshon
    for i in range(0,len(axuvdata.iloc[0,:])):
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
    filename_etendu='./axuv_data_201807/Etendu_volume_new.csv'
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
    npbright=nplowbright*10**(-3)/(10**5)/0.24*4*np.pi*(10**6)
    brightness=pd.DataFrame(npbright,
                            columns=['CH1','CH2','CH3','CH4',
                                     'CH5','CH6','CH7','CH8',
                                     'CH9','CH10','CH11','CH12',
                                     'CH13','CH14','CH15','CH16'])
    brightness['time']=list(axuvtime)
    print('Complete translation to brightness')

    
    return brightness


# In[ ]:




# In[ ]:




# In[ ]:



