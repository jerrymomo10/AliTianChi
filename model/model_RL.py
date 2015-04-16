# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 16:53:38 2015

@author: Administrator
"""
from numpy import *
from sklearn.linear_model import LogisticRegression 
import pandas as pd
import system_
import os
from feature import *
os.chdir('../data/feature')
system_.__clear_env()
#训练模型
# 添加behaes F1降低
features = ["buy_sum10","behaviors_sum10","buy_behavs","Item_sale10","Item_sale5","Item_sale3","Item_sale1","car5","car4","car3","car2","car1","buy5","buy4","buy3","buy2","buy1","last_time","I_order10","I_order5","I_order3","I_order1"]
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

