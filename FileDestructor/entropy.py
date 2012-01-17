import collections
import math

def calc_entropy(datadict, datalen):
    entropy = float(0)

    n = float(datalen)
    for value in datadict.values():
        p = value / n
        entropy += p * math.log(p, 2)
        
    return -1 * entropy

def entropy(data):
    count = collections.defaultdict(int)

    for byte in data:
        count[byte] += 1


    return calc_entropy(count, len(data))


