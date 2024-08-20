import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def sql(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    results = cur.fetchall()
    conn.close()

    if (cur.description): 
        column_names = [column[0] for column in cur.description]
        return [dict(zip(column_names, row)) for row in results]
    else:
        return cur.rowcount
    
# This is a basic implementation of a lexorank algorithm.
# Real apps would use a verified package or a richer implementation to handle resorting etc...
def calcLexorank(preceding_rank: str, following_rank: str | None) -> str:
    print(preceding_rank)
    print(following_rank)
    if following_rank == None or len(preceding_rank) < len(following_rank):
        return preceding_rank + 'a'
    else:
        return preceding_rank + 'n'