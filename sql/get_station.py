import pandas as pd
import json
from station_test import *

ll = []
with open('./center_sq_25.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

for i in content:
    print(get_station(i))
    ll.append(get_station(i)[0])# print(i)


station_save = json.dumps(ll, indent=3, ensure_ascii=False)
with open('station_5_25.json', 'w') as f:
    f.write(station_save)
