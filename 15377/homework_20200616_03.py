import pandas as pd

# Read information from csv
car_ori_pd = pd.read_csv(r'car_complain.csv')
print('原始数据'.center(30,'-'))
print(car_ori_pd)

# Prepossession
car_ori_pd['brand'].replace('一汽-大众','一汽大众',inplace=True)
car_ori_pd['brand'].replace('一汽-大众奥迪','一汽大众奥迪',inplace=True)

# split type of complaint
problem_pd =car_ori_pd.problem.str.get_dummies(',')
car_pre_pd = car_ori_pd.drop(columns='desc,problem,datetime,status'.split(',')).join(problem_pd)
print('处理后数据'.center(30,'-'))
print(car_pre_pd)

# brand complaints
c_brand_pd = car_pre_pd.groupby(['brand'])['id'].count().sort_values(ascending=False)
print('品牌投诉总数'.center(30,'-'))
print(c_brand_pd)
# model complaints
c_model_pd = car_pre_pd.groupby(['car_model'])['id'].count().sort_values(ascending=False)
print('车型投诉总数'.center(30,'-'))
print(c_model_pd)

# average of model complaints
ave_model = car_pre_pd.groupby(['brand','car_model'])['id'].agg('count').groupby('brand').mean().sort_values(ascending=False)
print('车型品牌平均投诉'.center(30,'-'))
print(ave_model)

