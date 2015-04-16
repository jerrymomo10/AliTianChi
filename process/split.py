# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:41:00 2015

@author: Administrator
"""
import pandas as pd
from datetime import *
import time
import system_
import os
os.chdir('d://tianchi/data')
system_.__clear_env()

# 分割的训练集数目
files = 22

#生成21个训练集 10为0-9打标签 30为 20-29打标签
df_train_user = pd.read_csv("train_paras_time_bprocess.csv")
df_items = pd.read_csv("tianchi_mobile_recommend_train_item.csv")
df_items = df_items.item_id.drop_duplicates()
a = pd.DataFrame()
a["item_id"] = df_items.values
df_items = a
os.chdir('./files')
for i in range(files):
    print "Split file: "+str(i)
    j = i+10
    if j != 31:
        df_set = df_train_user[(df_train_user.time>=i)&(df_train_user.time<j)]
        df_set.to_csv(str(j)+".csv",index=False)
        
        df_result = df_train_user[(df_train_user.time==j)&(df_train_user.behavior_type==4)][["user_id","item_id"]]
        df_result = df_result.drop_duplicates()
        #仅仅预测P集合
        df_result = pd.merge(left=df_result,right=df_items,how="inner").drop_duplicates()
        df_result.to_csv("result"+str(j)+".csv",index=False)
    else:
        df_set = df_train_user[(df_train_user.time>=i)&(df_train_user.time<j)]
        df_set.to_csv("test.csv",index=False)
        
os.chdir('d://tianchi/process')