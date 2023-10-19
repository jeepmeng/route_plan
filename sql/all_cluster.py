import pandas as pd
import os
from sklearn.cluster import KMeans
import json
import numpy as np

ll = []
with open('./all_location.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

for i in content.keys():
    # print(i)
    ll.append(content[i])
# print(content.keys())
print(ll)



cluster = KMeans(n_clusters=35, random_state=0)
cluster.fit(ll)
y_pred = cluster.labels_
centtrod = cluster.cluster_centers_
print(y_pred)
print(centtrod)
hh =[]
for i in centtrod:
    print()
    hh.append(str(i[0]) + ',' + str(i[1]))
# print(ll)

tt = json.dumps(hh, indent=3, ensure_ascii=False)
with open('center_35.json', 'w') as f:
    f.write(tt)
# print(centtrod+np.array(list_1))