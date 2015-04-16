# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 00:50:24 2015
时间转换 train_paras_time.csv 0-30
@author: Administrator
"""

import pandas as pd
from datetime import *
import time
import os
import system_
system_.__clear_env()
os.chdir('../data')

BEGINTIME = datetime(2014,11,18,0,0)

def paras_time(str_time):
    entry_time = datetime.strptime(str_time,"%Y-%m-%d %H")
    datetime_delta = (entry_time-BEGINTIME).days
    return int(datetime_delta)
df_train_user = pd.read_csv("tianchi_mobile_recommend_train_user.csv")

print "========================================\n"
print "Parasint time ...\n"
t0 = time.time()
df_train_user.time = df_train_user.time.map(lambda x: paras_time(x))
df_train_user.to_csv("train_paras_time.csv",index=False)
t1 = time.time()
print "Paras time Finished!\n"
print "It takes %f s to paras the time,generate 'train_paras_time.csv' in ../data" %(t1-t0)
os.chdir('../process')