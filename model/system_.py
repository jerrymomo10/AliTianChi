# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:08:54 2015

@author: Administrator
"""

def __clear_env(): 
    for key in globals().keys(): 
        if not key.startswith("__"): 
            globals().pop(key) 