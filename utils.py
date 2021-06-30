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
        limit = 0
        for i in reviews:
            if limit == limit:
                break
            data.append(i)
            limit += 1
    return data