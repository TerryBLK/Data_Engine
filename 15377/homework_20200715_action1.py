import pandas as pd
from fbprophet import Prophet

# read data file
train_ori = pd.read_csv("./train.csv")
print(train_ori.head())

# change the type of data
train_ori['Datetime'] = pd.to_datetime(train_ori.Datetime,format='%d-%m-%Y %H:%M')
train_ori.index = train_ori.Datetime
print(train_ori.head())

# drop useless column
train_ori.drop(['ID','Datetime'],axis=1,inplace=True)
print(train_ori)

# Resample the data by month
daily_train = train_ori.resample('D').sum()
print(daily_train.head())

# make up the final train data
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train.Count
daily_train.drop(['Count'],axis=1,inplace = True)
print(daily_train.head())

# Train the model by daily_train
md = Prophet(yearly_seasonality=True,seasonality_prior_scale=0.1)
md.fit(daily_train)

# predict the following 213 days
future = md.make_future_dataframe(periods=213)
forecast = md.predict(future)
print(forecast)

# plot result
md.plot(forecast).show()
md.plot_components(forecast).show()