# %%
import sqlite3

# %%
def sqlite_con():
    conn_ob = sqlite3.connect(r'C:\\sqlite\\dbs\\la-street-parking\\la-street-parking.db')
    conn_cursor = conn_ob.cursor()
    sample_insert_one = f"""
        INSERT INTO
            recent_occupancy
        VALUES
        (
            '1','0001',1,28000000,'VACANT',28374004
        )
    """
    conn_cursor.execute(sample_insert_one)
    conn_ob.commit()
    conn_ob.close()
sqlite_con()

# %%
def ro_sqlite(
    select_st = "select artistid, name from artists",
    def_db = "C:/sqlite/dbs/practice-chinook/chinook.db"
    # connect to sqlite3 db and execute one
    # iterates over rows by default, which we'd want for selecting
):
    import sqlite3
    conn_ob = sqlite3.connect(f"file:/{def_db}?mode=ro", uri=True)
    curs_ob = conn_ob.cursor()
    curs_ob.execute(select_st)
    tbl_rows = curs_ob.fetchall()
    for row in tbl_rows:
        print(row)
    conn_ob.close()
ro_sqlite('select artistid, name from artists')

# %%
def ex_sqlite(
    ex_st="select artistid, name from artists where name=?",
    lots=('BROCKHAMPTON',),
    def_db=r"C:\sqlite\dbs\practice-chinook\chinook.db"
    # connect to sqlite3 db and execute one
    # iterates over rows by default, which we'd want for selecting
):
    import sqlite3
    conn_ob = sqlite3.connect(def_db)
    curs = conn_ob.cursor()
    curs.execute(ex_st, lots)
    conn_ob.commit()
    conn_ob.close()



# %%
delete_adds = "delete from artists where name like ?"
ex_sqlite(delete_adds, ('BROCKHAMPTON',))
ex_sqlite(delete_adds, ('beyonce',))


# %%
def ex_many_sqlite(
        insert_st = f"insert into artists (name) values (?)",
        lots = [('BROCKHAMPTON',), ('BEYONCE',)],
        def_db = r"C:\sqlite\dbs\practice-chinook\chinook.db"
        # connect to sqlite3 db and execute many
):
    import sqlite3
    conn_ob = sqlite3.connect(def_db)
    with conn_ob:
        conn_ob.executemany(insert_st, lots)
    conn_ob.close()


# %%
ex_many_sqlite()


# %%