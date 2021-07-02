import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import json
import gzip
import re
import os

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield json.loads(l.strip())

def generate_data(paths, limit, parser):
    data = []
    for path in paths:
        reviews = parser(path = path)
        count = 0
        for i in reviews:
            if count == limit:
                break
            data.append(i)
            count += 1
    return data

def plot_counter(counter, n_most_common = 5, rotation_x_axis=45):
    """Plot dictionary Counter
    :param counter: Counter object
    :param n_most_common: Top most common words
    :param rotation_x_axis: Angle of ration x axis plot
    :return: plot, must write plt.show to display
    """
    top_items = counter.most_common(n_most_common)
    plt.xticks(rotation=rotation_x_axis)
    return plt.bar(*zip(*top_items))

def counter_len(word_counts):
    """Counts the lenght of the words
    :param word_counts: Counter object
    :return: Counter object with lengths instead of counts

    >>> counter_len(Counter({'hi':3, 'name':5}))
    Counter({'name': 4, 'hi': 2})
    """
    return Counter({x: len(x) for x in word_counts})