# %%
# connect to sqlite db in read-only mode
# should write a convertor function to pandas
# probably need to add parameter argument for where clause
def ro_sqlite(
    select_st="select artistid, name from artists",
    def_db="C:/sqlite/dbs/practice-chinook/chinook.db"
):
    import sqlite3
    conn_ob = sqlite3.connect(f"file:/{def_db}?mode=ro", uri=True)
    curs_ob = conn_ob.cursor()
    curs_ob.execute(select_st)
    tbl_rows = curs_ob.fetchall()
    for row in tbl_rows:
        print(row)
    conn_ob.close()

    return tbl_rows


# %%
# execute one, for example delete a row
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
    print(f'{curs.rowcount} row(s) affected')

    conn_ob.commit()
    conn_ob.close()


# %%
# execute many, for example insert multiple rows
def ex_many_sqlite(
        insert_st=f"insert into artists (name) values (?)",
        lots=[('BROCKHAMPTON',), ('BEYONCE',)],
        def_db=r"C:\sqlite\dbs\practice-chinook\chinook.db"
        # connect to sqlite3 db and execute many
):
    import sqlite3
    conn_ob = sqlite3.connect(def_db)
    with conn_ob:
        conn_ob.executemany(insert_st, lots)
    conn_ob.close()



# %%
if __name__ == "__main__":
    ro_sqlite('select artistid, name from artists')

    new_artists = [('BROCKHAMPTON',), ('Beyonce',)]
    ex_many_sqlite("insert into artists (name) values (?)", lots=new_artists)
    ro_sqlite('select artistid, name from artists')
    
    delete_adds = "delete from artists where name like ?"
    ex_sqlite(delete_adds, ('brockhampton',))
    ex_sqlite(delete_adds, ('beyonce',))


# %%
