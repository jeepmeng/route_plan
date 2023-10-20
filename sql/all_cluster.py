import pandas as pd
import os
from sklearn.cluster import KMeans
import json
import numpy as np

ll = []
def k_cluster():
    with open('./all_location.json', 'r') as f:
        content = f.read()
        content = json.loads(content)

    for i in content.keys():
        # print(i)
        ll.append(content[i])
    # print(content.keys())
    print(ll)



    cluster = KMeans(n_clusters=25, random_state=0)
    cluster.fit(ll)
    # y_pred = cluster.labels_
    centtrod = cluster.cluster_centers_
    # print(y_pred)
    # print(type(centtrod.tolist()))
    # print(centtrod.tolist())
    return centtrod.tolist()


if __name__ == '__main__':
    centtrod = k_cluster()

    hh =[]
    for i in centtrod:
        print()
        hh.append(str(i[0]) + ',' + str(i[1]))


    tt = json.dumps(hh, indent=3, ensure_ascii=False)
    with open('center_60.json', 'w') as f:
        f.write(tt)
