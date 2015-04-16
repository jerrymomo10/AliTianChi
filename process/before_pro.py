# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 21:06:59 2015
去掉那些30天无购买的用户 
@author: Administrator
"""

import pandas as pd
import os
import system_
system_.__clear_env()
os.chdir('../data')

df = pd.read_csv("train_paras_time.csv")
df2 = df[["user_id","behavior_type","time"]]
print "Total Behavior is: "+str(len(df))

buyers = df2['user_id']
buyers = buyers.drop_duplicates()
print "Total Buyers is: "+str(len(buyers))

df_buy = df2[df2.behavior_type==4]
buyers = df_buy['user_id']
buyers = buyers.drop_duplicates()
print "Left Buyers is: "+str(len(buyers))

a =pd.DataFrame()
a["user_id"] = buyers.values
df = pd.merge(left=a,right=df,how='left')
print "Left Behavior is: "+str(len(df))
df.to_csv("train_paras_time_bprocess.csv",index=False)
os.chdir('../process')