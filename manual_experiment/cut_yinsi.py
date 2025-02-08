import os
import json
root_path = '/Users/bytedance/Desktop/ICML_Fig/manual_experiment'
people = [os.path.join(root_path, x) for x in os.listdir(root_path) if not x.startswith('.') and not x.endswith('.py')]
packages = list()
for person in people:
    packages.extend([os.path.join(person, x) for x in os.listdir(person) if x.endswith('.log')])
for p in packages:
    with open(p, 'r') as r1:
        x = r1.read()
    x = x.replace('http://sys-proxy-rd-relay.byted.org:8118', '').replace('http://bytedpypi.byted.org', '').replace('byte', '')
    # print(x)
    with open(p, 'w') as w1:
        w1.write(x)
