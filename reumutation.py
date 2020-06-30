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
#Create bar graph showing those with mutations vs those without
#calculate total number of samples
totalsamples = len(df)


#calculate total num of mutations
mutationCount = df.count().sum()


#count number of samples with no mutations
countNan = totalsamples - mutationCount

#create bar graph
objects = ('Mutations','No Mutations')
y_pos = np.arange(len(objects))
position = [mutationCount,countNan]
plt.bar(y_pos,position,align='center',alpha = .5,color='b')
plt.xticks(y_pos,objects)
plt.ylabel('Num of Samples')
plt.title('Mutated vs Non-Mutated Samples')
plt.show

#frequency distribution best Laf
lAF = pd.read_excel(r'C:\Users\emmav\reumutation\dataset1.xlsx',index_col=None,na_values=['NaN'],usecols = "M,N:O")

freqTable = lAF.apply(lambda x: pd.cut(x, bins=[0,.1,.3,.4,.5]).value_counts()).add_prefix('count_')
print(freqTable)





