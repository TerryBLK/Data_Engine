import numpy as np
import pandas as pd

data = {'姓名':['张飞','关羽','刘备','典韦','许诸'],'语文':[68,95,98,90,80],
        '数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
student_pd = pd.DataFrame(data=data)
# print(student_pd)

# Describe the DataFrame of these 5 studens
# print(student_pd.describe())
print('平均成绩'.center(30,'-'))
print(student_pd[['语文','数学','英语']].mean())
print('最大成绩'.center(30,'-'))
print(student_pd[['语文','数学','英语']].max())
print('最小成绩'.center(30,'-'))
print(student_pd[['语文','数学','英语']].min())


# add a column for total
student_pd['SUM'] = student_pd[['语文','数学','英语']].sum(axis=1)

# sort by column "SUM"
sort_result = student_pd.sort_values(by=['SUM'],ascending=False)
sort_result = sort_result.reset_index(drop=True)
print('按总成绩排序'.center(30,'-'))
print(sort_result)

# Rank
student_pd['RANK'] = student_pd['SUM'].rank(ascending=False)
rank_result = student_pd.sort_values(by=['RANK'])
rank_result = rank_result.reset_index(drop=True)
print('排名'.center(30,'-'))
print(rank_result)



