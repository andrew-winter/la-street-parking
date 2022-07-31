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
# open db as read-only, supply query, qtupl, cpath
# if parameters are used, they must be supplied as a tuple
def read_sqlite(
    query=f"select * from artists where name=?",
    qtupl=None,
    cpath="C:/sqlite/dbs/practice-chinook/chinook.db"
):
    import sqlite3
    import pandas as pd
    
    conec = sqlite3.connect(f"file:/{cpath}?mode=ro", uri=True)
    df = pd.read_sql_query(sql=query, con=conec, params=qtupl)
    conec.commit()
    conec.close()
    return df

# %%
read_sqlite(
    query=f"""
        select *
        from artists
        where name like ?""",
    qtupl=("%bey%",)
)


# %%

read_sqlite(f"""select trackid from tracks""")
# %% 
# date range of current occupancy
min(current_occupancy.eventtime)
max(current_occupancy.eventtime)

# %%
squery = f"""
    select
        tra.trackid as track_id,
        tra.name as track_name,
        alb.albumid as album_id,
        alb.title_test as album_name,
        tra.genreid as genre_id,
        gen.name as genre_name
    from
        tracks as tra
    left join
        albums as alb
        on tra.albumid = alb.albumid
    left join
        genres as gen
        on tra.genreid = gen.genreid
    where
        gen.name in (?,?,?,?)
"""
stupl = ('Easy Listening', 'R&B/Soul', 'Sci Fi & Fantasy', 'Alternative')
read_sqlite(query=squery, qtupl=stupl)



# %%
# insert a row
test_insert = f"""insert into recent_occupancy (spaceid, last_query, eventtime, occupancystate, dt_mod) values(?,?,?,?,?)"""
test_lots = (
    current_occupancy.iloc[1,][0],
    0,
    6400,
    current_occupancy.iloc[1,][2],
    17000000
)

ex_sqlite(
    ex_st=test_insert,
    lots=test_lots,
    def_db=r"C:\sqlite\dbs\la-street-parking\la-street-parking_test.db"
)

# %%