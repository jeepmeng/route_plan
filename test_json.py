import pandas as pd
import json



# i = '柳影中学公交信息采集.xlsx'
with open('./school_location.json', 'r') as f:
    content = f.read()
    content = json.loads(content)
    for k,i in enumerate(content.keys()):
        # print(i)
        content[i]['school_id'] = k
    # data = json.dumps(data)
    print(content)
with open('./school_location.json', 'w') as f:
    json.dump(content, f ,ensure_ascii=False, indent=3)
    # new = json.dumps({**json.loads(content), **{"new_key": "new_value"}})



# with open('./school_location.json', 'r') as f:
#     content = f.read()
#     content = json.loads(content)
#     print(content)