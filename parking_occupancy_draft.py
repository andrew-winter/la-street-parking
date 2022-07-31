# %%
import datetime
from urllib.request import urlopen
import json
import pandas as pd



#%%
# query current occupancy
occ_response = urlopen('https://data.lacity.org/resource/e7h6-4a3e.json?$limit=10000')
occ_raw = json.loads(occ_response.read())
occ = pd.DataFrame(occ_raw)

# %%
# query parking policy
policy_response = urlopen('https://data.lacity.org/resource/s49e-q6j2.json?$limit=10000&$offset=0&$order=spaceid')
policy_raw = json.loads(policy_response.read())
policy = pd.DataFrame(policy_raw)

# %%
for i in [occ, policy]:
    distinct_spaceids = i['spaceid'].unique()
    print(i.__name__)
    if len(distinct_spaceids) == len(i.index):
        print('No duplicate space ids found')
    else:
        print('There are more rows than distinct space ids')



# %%
policy