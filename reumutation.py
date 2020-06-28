# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import matplotlib as plt
import numpy as np

#create dataframe from excel file using desired columns and drop empty cells
df = pd.read_excel(r'C:\Users\emmav\reumutation\dataset1.xlsx',index_col=None,na_values=['NaN'],usecols = "J,K:L")
df = df.dropna()

#store df in numpy arr; col 0 = overlappingGene, col 1 = knownCNV, col 2 = repeats
df_arr = df.to_numpy()
#print(df_arr[0][0])







