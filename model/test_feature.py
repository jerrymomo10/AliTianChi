# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 17:25:10 2015

@author: Administrator
"""

import pandas as pd
import system_
import os
from feature import *
os.chdir('../data/files')
system_.__clear_env()

i = 31
df_feature = pd.read_csv("test.csv")

#为验证集提取特征
os.chdir('..')
df_items = pd.read_csv("tianchi_mobile_recommend_train_item.csv")
df_items = df_items.item_id.drop_duplicates()
a = pd.DataFrame()
a["item_id"] = df_items.values
df_items = a

df_ui = df_feature[["user_id","item_id"]].drop_duplicates()
df_ui = pd.merge(left=df_ui,right=df_items,how="inner")
#只在P集合里的 适用在UI I 特征中
df_feature_item = pd.merge(left=df_feature,right=df_items,how="inner")

df_buy_sum10 = buy_sum10(df_feature)
df_test = pd.merge(left=df_ui,right=df_buy_sum10,how="left")
  
df_behavior_sum10 = behavior_sum10(df_feature)
df_test = pd.merge(left=df_test,right=df_behavior_sum10,how="left")

df_test["buy_behavs"] =  df_test.buy_sum10/df_test.behaviors_sum10

df_item1 = Item_sale(df_feature,i)
df_test = pd.merge(left=df_test,right=df_item1,how="left")

df_car = car(df_feature,i)
df_test = pd.merge(left=df_test,right=df_car,how="left")

df_buy = buy(df_feature,i)
df_test = pd.merge(left=df_test,right=df_buy,how="left")

df_orders = I_Orders(df_feature_item,i)    
df_test = pd.merge(left=df_test,right=df_orders,how="left")

#df_I_buyers = I_buyers(df_feature_item)
#df_test = pd.merge(left=df_test,right=df_I_buyers,how="left")

df_ui_sum = UI_Sum(df_feature_item,i)
df_test = pd.merge(left=df_test,right=df_ui_sum,how="left")

df_ui_last_time = last_time(df_feature_item,i)
df_test = pd.merge(left=df_test,right=df_ui_last_time,how="left")
    
df_test.fillna(0,inplace=True)  
os.chdir('feature') 
df_test.to_csv("test_feature.csv",index=False)
