# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:53:21 2015

@author: Administrator
"""
import pandas as pd
import system_
import os
from feature import *
os.chdir('../data')
system_.__clear_env()

predict_num = 0
hit_num = 0
result_num = 0
precision = 0
callrate = 0

#换验证集这个要改

x = pd.read_csv("predict_v_RL.csv")
y = pd.read_csv("predict_v_RF.csv")
z = pd.merge(left=x,right=y,how="inner")
z.to_csv("ensambel_predict_result.csv",index=False)

os.chdir('files')
df_result = pd.read_csv("result30.csv")
os.chdir('..')
df_predict = pd.read_csv("ensambel_predict_result.csv")

inner = pd.merge(left=df_result,right=df_predict,how="inner")

predict_num = len(df_predict)
print "ensambel predict_num is: ",predict_num
hit_num = len(inner)
print "ensambel hit_num is: ",hit_num
result_num = len(df_result)
print "ensambel total result num is: ",result_num 

if predict_num!=0:
    precision = float(hit_num)/predict_num
if result_num!=0:
    callrate = float(hit_num)/result_num
print "ensambel Precision is：",precision
print "ensambel Call rate is: ",callrate

if precision+callrate != 0:
    print "ensambel F1 is: ",2*precision*callrate/(precision+callrate),'\n'
else:
    print "ensambel F1 is: 0"
    
df_predict = pd.read_csv("predict_v_RL.csv")

inner = pd.merge(left=df_result,right=df_predict,how="inner")

predict_num = len(df_predict)
print "RL predict_num is: ",predict_num
hit_num = len(inner)
print "RL hit_num is: ",hit_num
result_num = len(df_result)
print "RL total result num is: ",result_num 

if predict_num!=0:
    precision = float(hit_num)/predict_num
if result_num!=0:
    callrate = float(hit_num)/result_num
print "RL Precision is：",precision
print "RL Call rate is: ",callrate

if precision+callrate != 0:
    print "RL F1 is: ",2*precision*callrate/(precision+callrate),'\n'
else:
    print "RL F1 is: 0"

df_predict = pd.read_csv("predict_v_RF.csv")

inner = pd.merge(left=df_result,right=df_predict,how="inner")

predict_num = len(df_predict)
print "RF predict_num is: ",predict_num
hit_num = len(inner)
print "RF hit_num is: ",hit_num
result_num = len(df_result)
print "RF total result num is: ",result_num 

if predict_num!=0:
    precision = float(hit_num)/predict_num
if result_num!=0:
    callrate = float(hit_num)/result_num
print "RF Precision is：",precision
print "RF Call rate is: ",callrate

if precision+callrate != 0:
    print "RF F1 is: ",2*precision*callrate/(precision+callrate),'\n'
else:
    print "RF F1 is: 0"