# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:31:55 2018

@author: Carsten Claussen
"""


import pandas as pd
import os


print(os.path)

#CSV_PATH = os.path.join('C:\\temp\\', 'dummydata.csv')
#cvs_file = os.path.join('C:\\dev\\workspace\\Blueprism\\', 'BPVWorkQueueItem_out.csv')
os.chdir('C:\\Users\\Carsten Claussen\\Documents\\GitHub\\blueprism\source')
cvs_file = os.path.join("..\\data\\BPVWorkQueueItem_out.csv")
#cvs_file = os.path.join("C:\\Users\\Carsten Claussen\\Documents\\GitHub\\blueprism\\data\\Workitems_smn.csv")
df = pd.read_csv(cvs_file,  encoding = "utf-8")

#df = pd.read_csv(cvs_file,  nrows=10000, encoding = "ISO-8859-1")
cvs_file = os.path.join("..\\data\\Workitems_smn.csv")
df_full = pd.read_csv(cvs_file,  nrows=104170, encoding = "utf-8")
df_full = pd.read_csv(cvs_file, encoding = "utf-8")
