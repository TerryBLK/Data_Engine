import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,scale
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


# 读入数据 Read the data from CSV
train_x = raw_data = pd.read_csv(r'L3/car_data.csv', encoding='gbk',index_col=0)
print(raw_data)


# 数据归一化 Data Normalization
min_max_scaler = MinMaxScaler()
train_df = min_max_scaler.fit_transform(raw_data)
print(train_df)

"""
# 手肘法分析
sse=[]
for k in range(1,11):
    kmean = KMeans(n_clusters=k)
    kmean.fit(train_df)
    sse.append(kmean.inertia_)
x = range(1,11)
plt.xlabel("k")
plt.ylabel('SSE')
plt.plot(x,sse,'o-')
plt.show()
""" # 结果先5组


# 聚类 K-Means cluster
kmean = KMeans(n_clusters=5)
kmean.fit(train_df)
predict_y = kmean.predict(train_df)
print(predict_y)

# 整合 Combine 'Predict_y' to raw_data
raw_data['聚类分析结果']=predict_y
print(raw_data)

# 输入 Out put the result
print('输入聚类结果'.center(20,"*"))
for i in range(5):
    print('第{}类'.format(i+1).center(10,'-'))
    print(raw_data[raw_data['聚类分析结果']==i])