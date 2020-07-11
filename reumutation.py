# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
#create dataframe from excel file using desired columns
dfControl = pd.read_excel(r'C:\Users\emmav\reumutation\flt3Controlpop.xlsx',index_col=None,na_values=['NaN'])

dfCancer = pd.read_excel(r'C:\Users\emmav\reumutation\amlmutation.xlsx',index_col=None,na_values=['NaN'],usecols = "D,G,O,P,AA,AB")
newlocations = []
locations = dfCancer['Protein Change']
for i in locations:
    num1 = i[1]
    num2 = i[2]
    num3 = i[3]
    sumnum = num1 + num2 + num3
    newlocations.append(sumnum)
dfCancer['locations']= newlocations
dfCancer = dfCancer.sort_values('locations', ascending = True)
#print(dfCancer)

def lollipop(df):

    missenserows = df[df['Mutation Type'] == 'Missense_Mutation']
    missenserows = missenserows.sort_values(by=['locations'])
    mvalues = missenserows['# Mut in Sample'].to_numpy()
    mlocation = missenserows["locations"].to_numpy()
    

    
    ifrows = df[df['Mutation Type'] == 'In_Frame_Ins']
    ifrows = ifrows.sort_values(by=['locations'])
    ifvalues = ifrows['# Mut in Sample'].to_numpy()
    iflocation = ifrows["locations"].to_numpy()



    nrows = df[df['Mutation Type'] == 'Nonsense_Mutation']
    nrows = nrows.sort_values(by=['locations'])
    nvalues = nrows['# Mut in Sample'].to_numpy()
    nlocation = nrows["locations"].to_numpy()

    
    f, ax = plt.subplots(sharex = True, figsize=(18,5))
    plt.stem(mlocation,mvalues,markerfmt='o', label='Missense')
    plt.stem(iflocation,ifvalues,markerfmt='o', label='In Frame')
    f = plt.stem(nlocation,nvalues,markerfmt='o', label='Nonsense')
   
    
    plt.legend()
    plt.show()

def main():
    lollipop(dfCancer)
    
if __name__ == "__main__":
    main()
