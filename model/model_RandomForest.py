# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 14:31:48 2015

@author: Administrator
"""

from numpy import *
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import system_
import os
from feature import *
os.chdir('../data/feature')
system_.__clear_env()

#训练模型
features = ["buy_sum10","behaviors_sum10","buy_behavs","Item_sale10","Item_sale5","Item_sale3","Item_sale1","car5","car4","car3","car2","car1","buy5","buy4","buy3","buy2","buy1",
"behav1","behav2","behav3","behav4","last_time","I_order10","I_order5","I_order3","I_order1"]
df_train = pd.read_csv("train_feature.csv")
df_validation  =pd.read_csv("validation_feature.csv")
ui = df_train[["user_id","item_id"]]
samples = df_train[features]
target = df_train["tag"]

clf = RandomForestClassifier(n_estimators=200)
clf.fit(samples, target)
validation_feature = df_validation[features]
x = clf.predict(validation_feature)
print x
validation_ui = df_validation[["user_id","item_id"]]
validation_ui["tag"] = x
validation_result = validation_ui[validation_ui.tag==1][["user_id","item_id"]]
os.chdir('..')
validation_result.to_csv("predict_v_RF.csv",index=False)