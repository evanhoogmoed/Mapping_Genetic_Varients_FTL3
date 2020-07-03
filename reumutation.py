# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import matplotlib as plt
import numpy as np


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#create dataframe from excel file using desired columns
dfControl = pd.read_excel(r'C:\Users\emmav\reumutation\flt3Controlpop.xlsx',index_col=None,na_values=['NaN'])
#print(dfControl)

dfCancer = pd.read_json(r'C:\Users\emmav\reumutation\mutations.2020-07-03.json')
#print(dfCancer)


#create frequency chart of mutations in control population
mutations = df['Annotation']
missenseCount = mutations.str.count('missense_variant').sum()
threeprimeCount = mutations.str.count('3_prime_UTR_variant').sum()
synonCount = mutations.str.count('synonymous_variant').sum()
frameshiftCount = mutations.str.count('frameshift_variant').sum()
stopgainCount = mutations.str.count('stop_gained').sum()
intronCount = mutations.str.count('intron_variant').sum()
spliceregionCount = mutations.str.count('splice_region_variant').sum()

f, ax = plt.subplots(figsize=(18,5))
objects = ('missense','3-prime','synonymous','frameshift','stop-gain','intron','splice-region')
y_pos = np.arange(len(objects))
position = [missenseCount,threeprimeCount,synonCount,frameshiftCount,stopgainCount,intronCount,spliceregionCount]
f = plt.bar(y_pos,position,align='center',alpha = .5,color='b')
plt.xticks(y_pos,objects)
plt.ylabel('Num of Samples')
plt.title('Frequency of Mutations')
plt.show

