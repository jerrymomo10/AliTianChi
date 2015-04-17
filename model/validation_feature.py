# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 17:25:10 2015

@author: Administrator
"""

import pandas as pd
import os
from feature import *
os.chdir('../data/files')

i = 30
df_feature = pd.read_csv("30.csv")

#为验证集提取特征
os.chdir('..')
df_items = pd.read_csv("tianchi_mobile_recommend_train_item.csv")
df_items = df_items.item_id.drop_duplicates()
df_items = df_items.to_frame()

df_ui = df_feature[["user_id","item_id"]].drop_duplicates()
df_ui = pd.merge(left=df_ui,right=df_items,how="inner")

df_feature_item = pd.merge(left=df_feature,right=df_items,how="inner")

#10天,5天,3天,1天的购买次数
U1 = buy_sum10(df_feature,i)
df_validation = pd.merge(left=df_ui,right=U1,how="left")
#10天,5天,3天,1天的点击次数
U2 = click_sum10(df_feature,i)
df_validation = pd.merge(left=df_validation,right=U2,how="left")
#10天,5天,3天,1天的点击收藏次数
U3 = collection_sum10(df_feature,i)
df_validation = pd.merge(left=df_validation,right=U3,how="left")
#10天,5天,3天,1天的点击加购物车次数
U4 = car_sum10(df_feature,i)
df_validation = pd.merge(left=df_validation,right=U4,how="left")
#10,5,3,1天的点击量 /购买量
df_validation["U_click/buy10"] =  df_validation.U_click_sum10/df_validation.U_buy_sum10
df_validation["U_click/buy5"] =  df_validation.U_click_sum5/df_validation.U_buy_sum5
df_validation["U_click/buy3"] =  df_validation.U_click_sum3/df_validation.U_buy_sum3
df_validation["U_click/buy1"] =  df_validation.U_click_sum1/df_validation.U_buy_sum1
#去除inf
df_validation["U_click/buy10"]=df_validation["U_click/buy10"].map(lambda x: fillinf(x))
df_validation["U_click/buy5"]=df_validation["U_click/buy5"].map(lambda x: fillinf(x))
df_validation["U_click/buy3"]=df_validation["U_click/buy3"].map(lambda x: fillinf(x))
df_validation["U_click/buy1"]=df_validation["U_click/buy1"].map(lambda x: fillinf(x))
#10,5,3,1天的收藏量 /购买量
df_validation["U_collection/buy10"] =  df_validation.U_collection_sum10/df_validation.U_buy_sum10
df_validation["U_collection/buy5"] =  df_validation.U_collection_sum5/df_validation.U_buy_sum5
df_validation["U_collection/buy3"] =  df_validation.U_collection_sum3/df_validation.U_buy_sum3
df_validation["U_collection/buy1"] =  df_validation.U_collection_sum1/df_validation.U_buy_sum1
    #去除inf
df_validation["U_collection/buy10"]=df_validation["U_collection/buy10"].map(lambda x: fillinf(x))
df_validation["U_collection/buy5"]=df_validation["U_collection/buy5"].map(lambda x: fillinf(x))
df_validation["U_collection/buy3"]=df_validation["U_collection/buy3"].map(lambda x: fillinf(x))
df_validation["U_collection/buy1"]=df_validation["U_collection/buy1"].map(lambda x: fillinf(x))
#10,5,3,1天的购物车量 /购买量
df_validation["U_car/buy10"] =  df_validation.U_car_sum10/df_validation.U_buy_sum10
df_validation["U_car/buy5"] =  df_validation.U_car_sum5/df_validation.U_buy_sum5
df_validation["U_car/buy3"] =  df_validation.U_car_sum3/df_validation.U_buy_sum3
df_validation["U_car/buy1"] =  df_validation.U_car_sum1/df_validation.U_buy_sum1
    #去除inf
df_validation["U_car/buy10"]=df_validation["U_car/buy10"].map(lambda x: fillinf(x))
df_validation["U_car/buy5"]=df_validation["U_car/buy5"].map(lambda x: fillinf(x))
df_validation["U_car/buy3"]=df_validation["U_car/buy3"].map(lambda x: fillinf(x))
df_validation["U_car/buy1"]=df_validation["U_car/buy1"].map(lambda x: fillinf(x)) 

df_behavior_sum10 = behavior_sum10(df_feature)
df_validation = pd.merge(left=df_validation,right=df_behavior_sum10,how="left")
#df_validation["buy_behavs"] =  df_validation.buy_sum10/df_validation.behaviors_sum10

df_item1 = Item_sale(df_feature,i)
df_validation = pd.merge(left=df_validation,right=df_item1,how="left")

df_car = car(df_feature,i)
df_validation = pd.merge(left=df_validation,right=df_car,how="left")

df_buy = buy(df_feature,i)
df_validation = pd.merge(left=df_validation,right=df_buy,how="left")

df_orders = I_Orders(df_feature_item,i)    
df_validation = pd.merge(left=df_validation,right=df_orders,how="left")

df_I_buyers = I_buyers(df_feature_item,i)
df_validation = pd.merge(left=df_validation,right=df_I_buyers,how="left")

df_ui_sum = UI_Sum(df_feature_item,i)
df_validation = pd.merge(left=df_validation,right=df_ui_sum,how="left")

df_ui_last_time = last_time(df_feature_item,i)
df_validation = pd.merge(left=df_validation,right=df_ui_last_time,how="left")
    
df_validation.fillna(0,inplace=True)  
os.chdir('feature') 
df_validation.to_csv("validation_feature.csv",index=False)
