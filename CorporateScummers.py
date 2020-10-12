import random
import matplotlib.pyplot as plt
import numpy as np


def calculate_prob(lst: list):
    res = dict()
    for nmbr in lst:
        for n in list(map(int, u'%s' % nmbr)):
            if res.get(n) is not None:
                res[n] += 1
            else:
                res[n] = 1
    return res


def show_probs(prbs: dict):
    for key in prbs.keys():
        plt.plot(key, prbs.get(key), marker="D")
    plt.show()


# как часть встречаются цифры 3, 4 и 5 в ряду 343, 535, 34
probs = calculate_prob([343, 535, 34])
print(probs)
show_probs(probs)

# цены колеблются от 1 до 2 тысяч
year = list(map(lambda x: random.randint(1000, 2001), range(1, 365)))
print(year[:10])
prob = calculate_prob(year)
show_probs(prob)

# считаем накопелнным итогом
progressive_total = 0
progressive_total_list = list()
for nmbr in year:
    progressive_total += nmbr
    progressive_total_list.append(progressive_total)

prob = calculate_prob(progressive_total_list)
show_probs(prob)

# Воруем немного денег и смотрим на распределение
fake_progressive_total = 0
fake_progressive_total_list = list()
for nmbr in year:
    fake_progressive_total += (nmbr - random.randint(0, int(nmbr / 2)))
    fake_progressive_total_list.append(fake_progressive_total)

prob = calculate_prob(fake_progressive_total_list)
show_probs(prob)
