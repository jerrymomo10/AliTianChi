# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 16:53:38 2015

@author: Administrator
"""
from numpy import *
from sklearn.linear_model import LogisticRegression 
import pandas as pd

import os
from feature import *
os.chdir('../data/feature')

#训练模型
# 添加behaes F1降低
features2 = ["U_buy_sum10","U_behaviors_sum10","buy_behavs","Item_sale10","Item_sale5","Item_sale3","Item_sale1","car5","car4","car3","car2","car1","buy5","buy4","buy3","buy2","buy1","last_time","I_order10",
"I_order5","I_order3","I_order1"]
features = ['U_buy_sum10', 'U_buy_sum5', 'U_buy_sum3',
       'U_buy_sum1', 'U_click_sum10', 'U_click_sum5', 'U_click_sum3',
       'U_click_sum1', 'U_collection_sum10', 'U_collection_sum5',
       'U_collection_sum3', 'U_collection_sum1', 'U_car_sum10',
       'U_car_sum5', 'U_car_sum3', 'U_car_sum1', 'U_click/buy10',
       'U_click/buy5', 'U_click/buy3', 'U_click/buy1',
       'U_collection/buy10', 'U_collection/buy5', 'U_collection/buy3',
       'U_collection/buy1', 'U_car/buy10', 'U_car/buy5', 'U_car/buy3',
       'U_car/buy1', 'U_behaviors_sum10', 'Item_sale10', 'Item_sale5',
       'Item_sale3', 'Item_sale1', 'car5', 'car4', 'car3', 'car2', 'car1',
       'buy5', 'buy4', 'buy3', 'buy2', 'buy1', 'I_order10', 'I_order5',
       'I_order3', 'I_order1', 'I_buyer10', 'I_buyer5', 'I_buyer3', 'I_buyer1',
       'behav1', 'behav2', 'behav3', 'behav4',
       'last_time']

df_train = pd.read_csv("train_feature.csv")
df_validation  =pd.read_csv("validation_feature.csv")
#数据归一化处理

ui = df_train[["user_id","item_id"]]
samples = df_train[features]
target = df_train["tag"]
classifier = LogisticRegression(penalty='l1',C=0.5)
classifier.fit(samples, target)  # 训练数据来学习，不需要返回值

validation_feature = df_validation[features]
x = classifier.predict(validation_feature)  # 测试数据，分类返回标记
print x
validation_ui = df_validation[["user_id","item_id"]]
validation_ui["tag"] = x
validation_result = validation_ui[validation_ui.tag==1][["user_id","item_id"]]
os.chdir('..')
validation_result.to_csv("predict_v_RL.csv",index=False)

