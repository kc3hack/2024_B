import sqlite3

###################################################################################################################################################################
#####################################################   これはDB内を簡易的に確認するためのプログラムファイルです   ###################################################
###################################################################################################################################################################

DATABASE = 'DB.db'

def list_tables_and_contents():
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()

    cursor.execute("SELECT * FROM sqlite_sequence;")
    sequence = cursor.fetchall()
    print("table name -> sqlite_sequence:")
    for item in sequence:
        print(item)
    print("\n")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        if table[0]=="sqlite_sequence":
            continue
        print(f"table name -> {table[0]}:")
        cursor.execute(f"SELECT * FROM {table[0]};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")

    con.close()

if __name__ == "__main__":
    list_tables_and_contents()
