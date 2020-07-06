# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create dataframe from excel file using desired columns
dfControl = pd.read_excel(r'C:\Users\emmav\reumutation\flt3Controlpop.xlsx',index_col=None,na_values=['NaN'])


#store json file into dataframe
dfCancer = pd.read_json(r'C:\Users\emmav\reumutation\cancermutations.json')

#compare DNA Change between Cancer and Control
#graph of Cancer
def basepairChangeCancerSum(dfCancer):
    dnaChangeCancer = dfCancer['mutation']
    variationCountA = dnaChangeCancer.str.count('A>').sum()
    variationCountT = dnaChangeCancer.str.count('T>').sum()
    variationCountC = dnaChangeCancer.str.count('C>').sum()
    variationCountG = dnaChangeCancer.str.count('G>').sum()

def basepairChangeControlSum(dfControl):
    #change control into same format
    dfControl['dnachange'] = dfControl['Reference'] + '>' + dfControl['Alternate']
    dnaChangeControl = dfControl['dnachange']
    variationControlCountA = dnaChangeControl.str.count('A>').sum()
    variationControlCountT = dnaChangeControl.str.count('T>').sum()
    variationControlCountC = dnaChangeControl.str.count('C>').sum()
    variationControlCountG = dnaChangeControl.str.count('G>').sum()

#create frequency chart of mutations in control population
def mutationChart(df):
    mutations = df['Annotation']
    missenseCount = mutations.str.count('missense_variant').sum()
    threeprimeCount = mutations.str.count('3_prime_UTR_variant').sum()
    synonCount = mutations.str.count('synonymous_variant').sum()
    frameshiftCount = mutations.str.count('frameshift_variant').sum()
    stopgainCount = mutations.str.count('stop_gained').sum()
    intronCount = mutations.str.count('intron_variant').sum()
    spliceregionCount = mutations.str.count('splice_region_variant').sum()
    fiveprimeCount = mutations.str.count('5_prime_UTR_variant').sum()


    f, ax = plt.subplots(figsize=(18,5))
    objects = ('missense','3-prime','synonymous','frameshift','stop-gain','intron','splice-region','5-prime')
    y_pos = np.arange(len(objects))
    position = [missenseCount,threeprimeCount,synonCount,frameshiftCount,stopgainCount,intronCount,spliceregionCount,fiveprimeCount]
    f = plt.bar(y_pos,position,align='center',alpha = .5,color='b')
    plt.xticks(y_pos,objects)
    plt.ylabel('Num of Samples')
    plt.title('Frequency of Mutations')
    plt.show


def main():
    mutationChart(dfControl)
    basepairChangeCancerSum(dfCancer)
    basepairChangeControlSum(dfControl)
    
if __name__ == "__main__":
    main()
