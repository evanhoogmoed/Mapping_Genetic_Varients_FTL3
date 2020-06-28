# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import matplotlib as plt
from pandas import DataFrame
import numpy as np

mydata = pd.read_excel("dataset1.xlsx")
df = DataFrame(mydata,columns = ['>chr','begin','end','avgNormalalizedCvg','relativeCvg','calledPloidy','calledCNVType','ploidyScore','CNVTypeScore','overlappingGene','knownCNV','repeats','bestLAF','lowLAF','highLAF'])
df = df.dropna(0)

print(df)

overlap = df['overlappingGene']
knownCNV = df['knownCNV']
repeats = df['repeats']

print(overlap)
print(knownCNV)
print(repeats)




