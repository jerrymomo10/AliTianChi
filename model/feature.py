# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:39:27 2015

@author: Administrator
"""
import pandas as pd
import random

#提取前十天的用户特征
"""
1.前十天的购买量 输入为十天的DF（U I B CU CI T） 输出为U  F F为十天的购买量
"""
def buy_sum10(df):
    df_buy_sum10 = df[["user_id","behavior_type","time"]]
    df_buy_sum10 = df_buy_sum10[df_buy_sum10.behavior_type==4][["user_id","time"]]
    x = df_buy_sum10.user_id.value_counts()
    df_buy_sum10 = pd.DataFrame()
    df_buy_sum10["user_id"] = x.index
    df_buy_sum10["buy_sum10"] = x.values
    return df_buy_sum10[["user_id","buy_sum10"]]
"""
2.用户购买行为占所有行为 输入为十天的DF（U I B CU CI T） 输出为U  F1  F1为十天的行为数 
"""
def behavior_sum10(df):
    t = ["user_id","behavior_type"]
    df_2 = df[t]
    x = df_2.user_id.value_counts()    
    a = pd.DataFrame()
    a["user_id"] = x.index
    a["behaviors_sum10"] = x.values
    return a
#提取前十天的商品特征
"""
1.十天商品的销量，五天的销量，三天的销量，最后一天的销量 输入为十天的DF（U I B CU CI T） 输出为U  F1 F2 F3 F4 
"""
def Item_sale(df,i):
    t = ["item_id","time"]
    df_2 = df[df.behavior_type==4][t]
    x = df_2.item_id.value_counts()
    a = pd.DataFrame()
    a["item_id"] = x.index
    a["Item_sale10"] = x.values
    df_2 = df_2[df_2.time>i-6]
    x = df_2.item_id.value_counts()
    b = pd.DataFrame()
    b["item_id"] = x.index
    b["Item_sale5"] = x.values
    df_2 = df_2[df_2.time>i-4]
    x = df_2.item_id.value_counts()
    c = pd.DataFrame()
    c["item_id"] = x.index
    c["Item_sale3"] = x.values 
    df_2 = df_2[df_2.time>i-2]
    x = df_2.item_id.value_counts()
    d = pd.DataFrame()
    d["item_id"] = x.index
    d["Item_sale1"] = x.values
    x = pd.merge(left=a,right=b,how="left")
    x = pd.merge(left=x,right=c,how="left")
    x = pd.merge(left=x,right=d,how="left")
    x.fillna(0,inplace=True)
    return x
"""
2.成交订单数 10 5 3 1 输入为十天的DF（U I B CU CI T） 输出为U  F1 F2 F3 F4 
"""
def I_Orders(df,i):
    t = ["item_id","user_id","time"]
    df_2 = df[df.behavior_type==4][t]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    df_4 = df_2["item_id"].to_frame().drop_duplicates()
    df_5 = pd.merge(left=df_3,right=df_4,how="right")
    x = df_5.item_id.value_counts()
    a = pd.DataFrame()
    a["item_id"] = x.index
    a["I_order10"] = x.values
    
    df_2 = df_2[df_2.time>i-6]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    df_4 = df_2["item_id"].to_frame().drop_duplicates()
    df_5 = pd.merge(left=df_3,right=df_4,how="right")
    x = df_5.item_id.value_counts()
    b = pd.DataFrame()
    b["item_id"] = x.index
    b["I_order5"] = x.values

    df_2 = df_2[df_2.time>i-4]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    df_4 = df_2["item_id"].to_frame().drop_duplicates()
    df_5 = pd.merge(left=df_3,right=df_4,how="right")
    x = df_5.item_id.value_counts()
    c = pd.DataFrame()
    c["item_id"] = x.index
    c["I_order3"] = x.values 
    
    df_2 = df_2[df_2.time>i-2]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    df_4 = df_2["item_id"].to_frame().drop_duplicates()
    df_5 = pd.merge(left=df_3,right=df_4,how="right")
    x = df_5.item_id.value_counts()
    d = pd.DataFrame()
    d["item_id"] = x.index
    d["I_order1"] = x.values
    x = pd.merge(left=a,right=b,how="left")
    x = pd.merge(left=x,right=c,how="left")
    x = pd.merge(left=x,right=d,how="left")
    x.fillna(0,inplace=True)
    return x
"""
3.购买人数10 5 3 1 输入为十天的DF（U I B CU CI T） 输出为U  F1 F2 F3 F4 
"""
def I_buyers(df,i):
    t = ["item_id","user_id","time"]
    df_2 = df[df.behavior_type==4][t]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    x = df_3.item_id.value_counts()
    a = pd.DataFrame()
    a["item_id"] = x.index
    a["I_buyer10"] = x.values
    
    df_2 = df_2[df_2.time>i-6]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    x = df_3.item_id.value_counts()
    b = pd.DataFrame()
    b["item_id"] = x.index
    b["I_buyer5"] = x.values

    df_2 = df_2[df_2.time>i-4]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    x = df_3.item_id.value_counts()
    c = pd.DataFrame()
    c["item_id"] = x.index
    c["I_buyer3"] = x.values 
    
    df_2 = df_2[df_2.time>i-2]
    df_3 = df_2[["item_id","user_id"]].drop_duplicates()
    x = df_3.item_id.value_counts()
    d = pd.DataFrame()
    d["item_id"] = x.index
    d["I_buyer1"] = x.values
    x = pd.merge(left=a,right=b,how="left")
    x = pd.merge(left=x,right=c,how="left")
    x = pd.merge(left=x,right=d,how="left")
    x.fillna(0,inplace=True)
    return x
#提取用户 商品特征
"""
1.倒数1 2 3 4 5 天添加购物车 输入为十天的DF（U I B CU CI T） 输出为U  F1 F2 F3 F4 F5  F1为最后一天加入购物车与否 
"""
def car(df,i):
    t = ["user_id","item_id","time"]
    df_2 = df[df.behavior_type==3][t]
    a = df_2[df_2.time==i-5][["user_id","item_id"]].drop_duplicates()
    a["car5"] = 1
    
    b = df_2[df_2.time==i-4][["user_id","item_id"]].drop_duplicates()
    b["car4"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-3][["user_id","item_id"]].drop_duplicates()
    b["car3"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-2][["user_id","item_id"]].drop_duplicates()
    b["car2"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-1][["user_id","item_id"]].drop_duplicates()
    b["car1"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    a.fillna(0,inplace=True)
    return a
"""
2. 倒数1 2 3 4 5 天购买 输入为十天的DF（U I B CU CI T） 输出为U I F1 F2 F3 F4 F5  F1为最后一天是否被购买 
"""
def buy(df,i):
    t = ["user_id","item_id","time"]
    df_2 = df[df.behavior_type==4][t]
    a = df_2[df_2.time==i-5][["user_id","item_id"]].drop_duplicates()
    a["buy5"] = 1
    
    b = df_2[df_2.time==i-4][["user_id","item_id"]].drop_duplicates()
    b["buy4"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-3][["user_id","item_id"]].drop_duplicates()
    b["buy3"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-2][["user_id","item_id"]].drop_duplicates()
    b["buy2"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    
    b = df_2[df_2.time==i-1][["user_id","item_id"]].drop_duplicates()
    b["buy1"] = 1
    a = pd.merge(left=a,right=b,how="outer")
    a.fillna(0,inplace=True)
    return a
"""
3.前十天累计的行为（1 2 3 4）  输入为十天的DF（U I B CU CI T） 输出为U I F1   F1累计点击 F2 收藏 F3购物车 F4购买
"""
def UI_Sum(df,i):
    t = ["user_id","item_id","behavior_type"]
    df_2 = df[t]
    df_3 = df_2[df_2.behavior_type==1][["user_id","item_id"]]
    df_3["behav1"] = 1
    a = df_3.behav1.groupby([df_3.user_id,df_3.item_id]).count()
    a.to_csv("temp.csv")
    b = pd.read_csv("temp.csv",header=None)
    c = pd.DataFrame()
    c["user_id"] = b[0]
    c["item_id"] = b[1]
    c["behav1"] = b[2]
    
    df_3 = df_2[df_2.behavior_type==2][["user_id","item_id"]]
    df_3["behav2"] = 1
    a = df_3.behav2.groupby([df_3.user_id,df_3.item_id]).count()
    a.to_csv("temp.csv")
    b = pd.read_csv("temp.csv",header=None)
    d = pd.DataFrame()
    d["user_id"] = b[0]
    d["item_id"] = b[1]
    d["behav2"] = b[2]
    
    df_3 = df_2[df_2.behavior_type==3][["user_id","item_id"]]
    df_3["behav3"] = 1
    a = df_3.behav3.groupby([df_3.user_id,df_3.item_id]).count()
    a.to_csv("temp.csv")
    b = pd.read_csv("temp.csv",header=None)
    e = pd.DataFrame()
    e["user_id"] = b[0]
    e["item_id"] = b[1]
    e["behav3"] = b[2]
    
    df_3 = df_2[df_2.behavior_type==4][["user_id","item_id"]]
    df_3["behav4"] = 1
    a = df_3.behav4.groupby([df_3.user_id,df_3.item_id]).count()
    a.to_csv("temp.csv")
    b = pd.read_csv("temp.csv",header=None)
    f = pd.DataFrame()
    f["user_id"] = b[0]
    f["item_id"] = b[1]
    f["behav4"] = b[2]
    
    x = pd.merge(left=c,right=d,how="outer")
    x = pd.merge(left=x,right=e,how="outer")
    x = pd.merge(left=x,right=f,how="outer")
    x.fillna(0,inplace=True)
    return x
"""
4.第一次访问到最后一次访问的时间间隔 输入为十天的DF（U I B CU CI T） 输出为U I F1   F1第一次访问到最后一次访问的时间间隔
"""

"""
5.最后一次访问到第十天的时间间隔 输入为十天的DF（U I B CU CI T） 输出为U I F1   F1最后一次访问到第十天的间隔
"""
def last_time(df,i):
    t = ["user_id","item_id"]
    #最后一天访问的UI
    df_1 = df[(df.time==(i-1))&(df.behavior_type!=1)][t].drop_duplicates()
    df_1["last_time"]=1
    df_ui = df_1
    
    df_2 = df[(df.time==(i-2))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_1,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=2
    df_ui = pd.concat([df_1,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-3))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=3
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-4))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=4
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-5))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=5
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)

    df_2 = df[(df.time==(i-6))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=6
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-7))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=7
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-8))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=8
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-9))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=9
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    
    df_2 = df[(df.time==(i-10))&(df.behavior_type!=1)][t].drop_duplicates()
    df_2 = pd.merge(left=df_ui,right=df_2,how="right")
    df_2.fillna(0,inplace=True)
    df_2 = df_2[df_2.last_time==0][t].drop_duplicates()
    df_2["last_time"]=10
    df_ui = pd.concat([df_ui,df_2],ignore_index=True)
    return df_ui

