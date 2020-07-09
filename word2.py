import re

with open("dataset_3363_3.txt", 'r+') as f:
    s = re.split(map(lambda i: i.strip('.,!?'), f.read().lower()))
    m = max(sorted(s), key = lambda j: s.count(j))
    print("%s %d" % (m, s.count(m)))