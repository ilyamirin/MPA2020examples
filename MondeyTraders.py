from random import choice, randint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def calculate_prob(lst: list):
    res = dict()
    for nmbr in lst:
        if res.get(nmbr) is not None:
            res[nmbr] += 1
        else:
            res[nmbr] = 1
    return res


def show_probabilities(prbs: dict):
    for key in prbs.keys():
        plt.plot(key, prbs.get(key), marker="D")
    plt.show()


# забираем курсы валют с августа 1998
rates = np.genfromtxt('https://raw.githubusercontent.com/ilyamirin/Taleb/master/usd_quotes.csv', delimiter=';',
                      dtype=None, encoding='utf-8')


def buy_dollars(bucket: dict, rate: float):
    amount = randint(0, bucket['r'])
    d = bucket['d'] + int(amount / rate)
    r = bucket['r'] - amount
    t = d + int(r / rate)
    return {'n': bucket['n'], 'd': d, 'r': r, 't': t}


print(buy_dollars({'d': 0, 'r': 100, 'n': 123}, 2))
buy_spree = list(map(lambda x: buy_dollars({'d': 0, 'r': 100, 't': 200, 'n': x}, 2.0), range(0, 1000)))
pd.DataFrame.from_records(buy_spree).plot(kind='scatter', x='d', y='n')
plt.show()


def buy_rubles(bucket: dict, rate: float):
    amount = randint(0, bucket['d'])
    d = bucket['d'] - amount
    r = bucket['r'] + int(amount * rate)
    t = d + int(r / rate)
    return {'n': bucket['n'], 'd': d, 'r': r, 't': t}


print(buy_rubles({'d': 10, 'r': 0, 'n': 321}, 2))

# TODO: add leverage options

start_dollars = 20000
# рубль упал в 20 раз с 1998 года
start_rubles = 100
start_total = start_dollars + (start_rubles / rates[-1][1])
traders = list(map(lambda x: {'d': start_dollars, 'r': start_rubles, 'n': x}, range(0, 1000)))

history = dict()
for rate in reversed(rates):
    history[rate[0]] = len(traders)
    new_gen = list()
    for trader in traders:
        new_trader = None
        if choice(('D', 'R')) == 'D':
            new_trader = buy_dollars(trader, rate[1])
        else:
            new_trader = buy_rubles(trader, rate[1])
        if new_trader['t'] != 0:
            new_gen.append(new_trader)

    traders = new_gen

print(len(traders))
pd.DataFrame.from_dict(history, orient='index').plot(kind='line')
plt.show()

result = pd.DataFrame.from_records(traders)
sls = 't'
print("max= %s" % result[sls].max())
print("It is  %d per cents of start amount" % (result[sls].max() / start_total * 100))
print("sum= %s" % result[sls].sum())
print("richest= %d per cent of the whole" % (result[sls].max() / result[sls].sum() * 100))
print(result.sort_values(sls).tail())
#print("------------------")
#print(result.groupby(sls).count()['n'])
