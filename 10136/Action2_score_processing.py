#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = {'chinese':[80,56,63,95,88],'math':[55,89,99,86,77],'english':[71,56,89,96,85]}
df = DataFrame(data, index = ['guanyu','zhangfei','zhaoyun','dianwei','zhangliao'], columns = ['chinese','math','english'])
print (df)

# 成绩的平均值，方差等的统计结果输出
print (df.describe())

# 每个人各科成绩的总分及平均值
chengji = df[['chinese','math','english']]
print (chengji)
df['total'] = chengji.sum(axis=1)
df['average'] = chengji.mean(axis=1)
print (df)

# 按照每个人各科成绩的总分排序
df.sort_values('total', ascending=False)

