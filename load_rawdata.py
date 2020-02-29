import pandas as pd
import numpy as np
import os
from os.path import join

def get_some_file(**kws):
    """ Given data folder, return some data for tests.
    This time we have one file, so return first one from list
    """
    basedir = kws.get('basedir','../../data')
    ld = os.listdir(basedir)
    lda = [i for i in ld if i.startswith('AXUV')]
    return join(basedir,lda[0])

def read_axuv_raw(fpath,**kws):
    """ Read AXUV raw data from the given file path
    """
    # define column names
    # TODO: automatic detection of columns
    colind = ['No','Date','Time','us']
    colch  = [f'CH{i}' for i in range(1,17)]
    colnan = [f'nan{i}' for i in range(1,32-4-15)]
    columns = colind + colch + colnan

    data = pd.read_csv(
        fpath,
        encoding = 'cp932',
        skiprows = 46,
        names = columns
    )
    # remove empty columns (these are from Alarms)
    data = data.drop(columns = colnan)
    # calculate time from sampling time and data length (assumin even sampling)
    t = np.linspace(0,data.shape[0]*(data['us'][1]-data['us'][0])*1e-6,data.shape[0])
    # remove Date-Time and number columns
    data = data.drop(columns = colind)
    # insert consequent time column
    data.insert(0,'time',t)
    # subtract offset (mean value for 100 points for all channels)
    data.iloc[:,1:] = data.drop(columns='time').sub(
        data.drop(columns='time').iloc[:100,:].mean())
    return data
