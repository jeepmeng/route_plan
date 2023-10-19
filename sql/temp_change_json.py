import pandas as pd
import json

ll = []
with open('./all_location.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

for i in content.items():
    ll.append(str(i[-1][0])+','+str(i[-1][1]))
print(ll)


hh = json.dumps(ll, indent=3, ensure_ascii=False)
with open('hh.json', 'w') as f:
    f.write(hh)
# print(content.items())