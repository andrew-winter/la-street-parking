# %%
import datetime
import numpy as np
import pandas as pd
from functions.page_soda import page_soda
from functions.read_soda_csv import read_soda_csv
from functions.sqlite_udfs import ro_sqlite
from functions.sqlite_udfs import ex_sqlite

# %%
# query current occupancy-- 5k+ rows
occupancy_ends = page_soda(
    endpoint='https://data.lacity.org/resource/e7h6-4a3e.csv?',
    limit=10000, order_by='spaceid')
current_occupancy = pd.concat(
    [read_soda_csv(j) for j in occupancy_ends], axis=0)
current_occupancy

# %%
# query parking policy-- 34k+ rows
policy_ends = page_soda(
    endpoint='https://data.lacity.org/resource/s49e-q6j2.csv?',
    limit=50000, order_by='spaceid')
policy = pd.concat(
    [read_soda_csv(j) for j in policy_ends],
    axis=0, ignore_index=True)
policy

# %%
for i in [current_occupancy, policy]:
    distinct_spaceids = i['spaceid'].unique()
    if len(distinct_spaceids) == len(i.index):
        print('No duplicate space ids found')
    else:
        print('There are more rows than distinct space ids')


# %%
merge_try = policy.merge(current_occupancy, how='left', on='spaceid')
merge_try[merge_try['eventtime'].notnull()]

merge_try2 = current_occupancy.merge(policy, how='left', on='spaceid')
merge_try3 = policy.merge(current_occupancy, how='inner', on='spaceid')

merge_try4 = current_occupancy.merge(policy, how='inner', on='spaceid')



# %%
cids = ['CB12', 'CB1203', 'CB1204',
    'CB1205', 'CB1267A', 'CB1267C']
merge_try2[merge_try2['spaceid'].isin(cids)]

merge_try4[merge_try4['spaceid'].isin(cids)]


# %%
join_attempts = [merge_try, merge_try2, merge_try3, merge_try4]
for i in join_attempts:
    print(len(i.index))
    print(i.value_counts(['occupancystate'], dropna=False))
    print('\n' * 2)


# %%
ids_left = []
ids_inner = []

for i, j in enumerate([merge_try2, merge_try4]):
    j.sort_values(['spaceid'], inplace=True)
    for er in range(len(j.index)):
        space_add = j.iloc[er]['spaceid']
        if i < 1:
            ids_left.append(space_add)
        elif i == 1:
            ids_inner.append(space_add)
        
print(len(ids_left))
print(len(ids_inner))

# %%
#f'ids_left: {ids_left}'
#f'ids_inner: {ids_inner}'
for i in ids_left:
    if i not in ids_inner:
        print(i)

# %%
# every spaceid in ids_inner is in ids_left, it seems
for i in ids_inner:
    if i not in ids_left:
        print(i)

# %%
merge_try2.iloc[4]['spaceid']

#

# %%


 # %%


  # %%
