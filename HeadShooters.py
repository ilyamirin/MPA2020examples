from random import choice, randint
from _datetime import datetime
import matplotlib.pyplot as plt


def fire(in_gamblers):
    lucky_ones = set()
    for gambler in in_gamblers:
        if choice((0, 0, 0, 0, 0, 1)) == 0:
            lucky_ones.add(gambler)
    return lucky_ones


def calculate_prob(lst: list):
    res = dict()
    for nmbr in lst:
        if res.get(nmbr) is not None:
            res[nmbr] += 1
        else:
            res[nmbr] = 1
    return res


def show_probs(prbs: dict):
    for key in prbs.keys():
        plt.plot(key, prbs.get(key), marker="D")
    plt.show()


intersection = set()
last_gens = list()
for k in range(0, 1000):
    history = list()
    gamblers = set(map(lambda x: randint(0, 999999999) + datetime.utcnow().timestamp(), range(1, 10000)))
    for g in range(0, 100):
        history.append((g, gamblers))
        gamblers = fire(gamblers)
        intersection = history[0][1].intersection(gamblers)
        if len(intersection) == 0:
            # print('Last generation is %s' % g)
            last_gens.append(g)
            break

probs = calculate_prob(last_gens)
print(probs)
show_probs(probs)
