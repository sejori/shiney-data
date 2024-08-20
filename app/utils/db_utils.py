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