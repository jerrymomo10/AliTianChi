# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:49:08 2015

@author: jerry
"""
#build features by x.csv
import pandas as pd
import random
import os
from feature import *
os.chdir('../data')
    
j = 10 
#为每一个训练集打标签
df_items = pd.read_csv("tianchi_mobile_recommend_train_item.csv")
df_items = df_items.item_id.drop_duplicates()
a = pd.DataFrame()
a["item_id"] = df_items.values
df_items = a
df_trains = pd.DataFrame()
os.chdir('files')
#20 不包括30的数据 21 包含30号的
for x in range(20):
    i = j+x
    print "Trains "+str(x+1)
    #提取最后一天的购买记录为前十天打标签
    df_tag = pd.read_csv("result"+str(i)+".csv")
    df_tag["tag"] = 1

    df_feature = pd.read_csv(str(i)+".csv")
    #只在P集合里的 适用在UI I 特征中
    df_feature_item = pd.merge(left=df_feature,right=df_items,how="inner")
    
    #为前十天打标签 预测的UI为前十天有行为的
    df_ui = df_feature[["user_id","item_id"]].drop_duplicates()
    df_ui = pd.merge(left=df_ui,right=df_items,how="inner")

    df_ui_tag = pd.merge(left=df_ui,right=df_tag,how="left")
    df_ui_tag.fillna(0,inplace=True)

    #Features 不要只 与 商品 会丢失用户的信息
    #df_ui_tag 为2万左右 预测这2万即可 其中只有113人为正样本 存在正负样本失衡(1:180) 考虑用户剔除和样本抽样
    #抽样 负样本随机抽样 变为正负为1:10 UI变为1463
    df_ui_tag_p = df_ui_tag[df_ui_tag.tag==1]
    df_ui_tag_n = df_ui_tag[df_ui_tag.tag==0]
    lp = len(df_ui_tag_p)
    ln = len(df_ui_tag_n)
    if float(ln)/lp > 15:
        a = range(0,ln)
        slice = random.sample(a,lp*15)    
        df_ui_tag_n = df_ui_tag_n.iloc[slice]
        df_ui_tag = pd.concat([df_ui_tag_p,df_ui_tag_n],ignore_index=True)
    
    #最后汇总时添加
    #10天,5天,3天,1天的购买次数
    U1 = buy_sum10(df_feature,i)
    df_train = pd.merge(left=df_ui_tag,right=U1,how="left")
    #10天,5天,3天,1天的点击次数
    U2 = click_sum10(df_feature,i)
    df_train = pd.merge(left=df_train,right=U2,how="left")
    #10天,5天,3天,1天的点击收藏次数
    U3 = collection_sum10(df_feature,i)
    df_train = pd.merge(left=df_train,right=U3,how="left")
    #10天,5天,3天,1天的点击加购物车次数
    U4 = car_sum10(df_feature,i)
    df_train = pd.merge(left=df_train,right=U4,how="left")
    #10,5,3,1天的点击量 /购买量
    df_train["U_click/buy10"] =  df_train.U_click_sum10/df_train.U_buy_sum10
    df_train["U_click/buy5"] =  df_train.U_click_sum5/df_train.U_buy_sum5
    df_train["U_click/buy3"] =  df_train.U_click_sum3/df_train.U_buy_sum3
    df_train["U_click/buy1"] =  df_train.U_click_sum1/df_train.U_buy_sum1
    #去除inf
    df_train["U_click/buy10"]=df_train["U_click/buy10"].map(lambda x: fillinf(x))
    df_train["U_click/buy5"]=df_train["U_click/buy5"].map(lambda x: fillinf(x))
    df_train["U_click/buy3"]=df_train["U_click/buy3"].map(lambda x: fillinf(x))
    df_train["U_click/buy1"]=df_train["U_click/buy1"].map(lambda x: fillinf(x))
    #10,5,3,1天的收藏量 /购买量
    df_train["U_collection/buy10"] =  df_train.U_collection_sum10/df_train.U_buy_sum10
    df_train["U_collection/buy5"] =  df_train.U_collection_sum5/df_train.U_buy_sum5
    df_train["U_collection/buy3"] =  df_train.U_collection_sum3/df_train.U_buy_sum3
    df_train["U_collection/buy1"] =  df_train.U_collection_sum1/df_train.U_buy_sum1
        #去除inf
    df_train["U_collection/buy10"]=df_train["U_collection/buy10"].map(lambda x: fillinf(x))
    df_train["U_collection/buy5"]=df_train["U_collection/buy5"].map(lambda x: fillinf(x))
    df_train["U_collection/buy3"]=df_train["U_collection/buy3"].map(lambda x: fillinf(x))
    df_train["U_collection/buy1"]=df_train["U_collection/buy1"].map(lambda x: fillinf(x))
    #10,5,3,1天的购物车量 /购买量
    df_train["U_car/buy10"] =  df_train.U_car_sum10/df_train.U_buy_sum10
    df_train["U_car/buy5"] =  df_train.U_car_sum5/df_train.U_buy_sum5
    df_train["U_car/buy3"] =  df_train.U_car_sum3/df_train.U_buy_sum3
    df_train["U_car/buy1"] =  df_train.U_car_sum1/df_train.U_buy_sum1
        #去除inf
    df_train["U_car/buy10"]=df_train["U_car/buy10"].map(lambda x: fillinf(x))
    df_train["U_car/buy5"]=df_train["U_car/buy5"].map(lambda x: fillinf(x))
    df_train["U_car/buy3"]=df_train["U_car/buy3"].map(lambda x: fillinf(x))
    df_train["U_car/buy1"]=df_train["U_car/buy1"].map(lambda x: fillinf(x)) 
    
    df_behavior_sum10 = behavior_sum10(df_feature)
    df_train = pd.merge(left=df_train,right=df_behavior_sum10,how="left")
    
    df_I_buyers = I_buyers(df_feature_item,i)
    df_train = pd.merge(left=df_train,right=df_I_buyers,how="left")        
    
    df_item1 = Item_sale(df_feature,i)
    df_train = pd.merge(left=df_train,right=df_item1,how="left")
    
    df_car = car(df_feature,i)
    df_train = pd.merge(left=df_train,right=df_car,how="left")
    
    df_buy = buy(df_feature,i)
    df_train = pd.merge(left=df_train,right=df_buy,how="left")
    
    df_orders = I_Orders(df_feature_item,i)    
    df_train = pd.merge(left=df_train,right=df_orders,how="left")

    df_ui_sum = UI_Sum(df_feature_item,i)
    df_train = pd.merge(left=df_train,right=df_ui_sum,how="left")    
    
    df_ui_last_time = last_time(df_feature_item,i)
    df_train = pd.merge(left=df_train,right=df_ui_last_time,how="left")
    
    
    df_train.fillna(0,inplace=True)
    df_trains = pd.concat([df_trains,df_train],ignore_index=True)
    
os.chdir('../feature') 
df_trains.to_csv("train_feature.csv",index=False)

