# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:47:39 2020

@author: Behnaz
"""


import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

file_path_pandemics = os.path.abspath("pandemics")
file_path_index = os.path.abspath("indeces")

data_pandemic = pd.read_csv(os.path.join(file_path_pandemics, 'PandemicData.csv'))#, parse_dates=['Date'], index_col='Date')

data_index = pd.read_csv(os.path.join(file_path_index, 'Data.csv'))#, parse_dates=['Date'], index_col='Date')
"""this chunck is for plot if  we read csv file as timeseries 
#plot index data
plt.subplot(221)
ts_index=data_index[data_index.Country.eq("Canada")]
ts_index = ts_index["Price"]
plt.plot(ts_index["2014"])

#plot pandemic data
plt.subplot(222)

ts_pandemic = data_pandemic[data_pandemic.Pandemic.eq("Ebola")]
ts_pandemic = data_pandemic[data_pandemic.Country.eq("Liberia")]
ts = ts_pandemic["ActiveCases"]
plt.plot(ts["2014"])
"""
"""this chunck is for plot if we don't read csv file as timeseries 
#worldwide pandemics' data
pandemicd = data_pandemic
pandemicd=pandemicd.groupby(['Date','Pandemic'],as_index=False).sum()
pandemicd=pandemicd[pandemicd.Pandemic.eq("Covid")]
pandemicd = pandemicd.drop(['Pandemic'],1)

#index market for one country
marketd = data_index
marketd=marketd[marketd.Country.eq("Germany")]
marketd = marketd.drop(['Change','Low','Open','Volume','High','Country'], 1)

#join two time series
result = pd.merge(pandemicd, marketd, how='inner', on=['Date'])

# specify columns to plot
values=result.values

groups = [1, 2,3]
i = 1
# plot each column
plt.figure()
for group in groups:
	plt.subplot(len(groups), 1, i)
	plt.plot(values[:, group])
	plt.title(result.columns[group], y=0.5, loc='left')
	i += 1
plt.show()
"""

"""LSTM
# prepare data for lstm
# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

# load dataset
dataset = result
dataset=dataset.set_index('Date')
#dataset.index = pd.to_datetime(dataset['Date'])
values = dataset.values


# frame as supervised learning
reframed = series_to_supervised(values, 1, 1)

# split into train and test sets
values = reframed.values

n_train = 150
train = values[:n_train, :]
test = values[n_train:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)


# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# plot history
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
"""
























