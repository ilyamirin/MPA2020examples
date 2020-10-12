import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn import linear_model


def print_list(lst: list):
    for element in lst:
        print(element)


base_path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
            '/csse_covid_19_time_series/'
confirmed_data_path = base_path + 'time_series_covid19_confirmed_global.csv'
recovered_data_path = base_path + 'time_series_covid19_recovered_global.csv'

data = pd.read_csv(confirmed_data_path)

mean = data.iloc[0:, 4:170].values.mean()
data_x = data.iloc[0:, 4:169].values / mean
data_y = data.iloc[0:, 5:170].values / mean

reg = linear_model.LinearRegression()
reg.fit(list(map(lambda x: [x], data_x.flatten())), data_y.flatten())

print((reg.predict([[969]]) - 981) / 981)
print((reg.predict([[922853]]) - 927745) / 927745)
print((reg.predict([[1285084]]) - 1298718) / 1298718)


# проверяем точность модели
data_x = data.iloc[0:, 169:-1].values.flatten()
data_y = data.iloc[0:, 170:].values.flatten()
total_m = 0
for i in range(0, len(data_x)):
    if data_y[i] == data_x[i] == 0:
        continue
    if ((data_y[i] - data_x[i]) / data_y[i]) > 0.1:
        continue
    p = reg.predict([[data_x[i]]])
    m = abs(p - data_y[i]) / data_y[i]
    if m > 0.012:
        total_m += m[0]
    plt.plot(i, total_m, 'r.')
print('Total mistake:', total_m)
plt.ylabel('Total mistake')
plt.show()

# ищем аномалии
for i in range(0, len(data_x)):
    if data_y[i] == data_x[i] == 0:
        continue
    m = (data_y[i] - data_x[i]) / data_y[i]
    if m > 0.1:
        plt.plot(i, m, 'r.')
        print("i=%d %d - %d = |%r|" % (i, data_x[i], data_y[i], m))
plt.ylabel('Data breaks')
plt.show()

s = 220
result = list()
for i in range(0, days):
    n = reg.predict([[s]])[0]
    result.append(int(n))
    s = n

confirmed = predict(confirmed_data_path, 100)
recovered = predict(recovered_data_path, 100)

print_list(confirmed)
# print('-----------------------------------------------')
# print_list(recovered)

data = pd.read_csv(confirmed_data_path)
for d in range(171, 267):
    data.iloc[0:, d]
    print((reg.predict([[969]]) - 981) / 981)
