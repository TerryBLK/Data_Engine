import pandas as pd
import numpy as np
from efficient_apriori import apriori

# Load CSV files
data_ori = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
print(data_ori.head(3))
print(data_ori.shape)

# 将数据放到trainsactions里
trainsacations =[]
for i in range(0,data_ori.shape[0]):
    temp = []
    for j in range(0,20):
        if str(data_ori.values[i,j])!='nan':
            temp.append(str(data_ori.values[i,j]))
    trainsacations.append(temp)
print(trainsacations)

# 挖掘频繁项集与关联规则 apriori
itemsets , rules = apriori(trainsacations,min_support=0.05,min_confidence=0.2)
print('频繁项集：',itemsets)
print('关联规则：',rules)


