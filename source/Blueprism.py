# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:31:55 2018

@author: Carsten Claussen
"""


import pandas as pd
import os

#CSV_PATH = os.path.join('C:\\temp\\', 'dummydata.csv')
cvs_file = os.path.join('C:\\dev\\workspace\\Blueprism\\', 'BPVWorkQueueItem_out.csv')
df = pd.read_csv(cvs_file,  encoding = "ISO-8859-1")

#df = pd.read_csv(cvs_file,  nrows=10000, encoding = "ISO-8859-1")
df = pd.read_csv(cvs_file,  nrows=10000, encoding = "ISO-8859-1")
