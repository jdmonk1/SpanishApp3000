import psycopg2

def start():
    connect_str = "dbname='postgres' user='postgres' host='localhost' port='5439'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # remove a table with a single column called "tutorials"
    cursor.execute("""DROP TABLE IF EXISTS accuracyfreqency;""")
    cursor.execute("""DROP TABLE IF EXISTS flashcardstats;""")
    cursor.execute("""DROP TABLE IF EXISTS flashcardsverbs;""")
    cursor.execute("""DROP TABLE IF EXISTS listtemp;""")
    cursor.execute("""DROP TABLE IF EXISTS profile;""")
    cursor.execute("""DROP TABLE IF EXISTS rated;""")
    cursor.execute("""DROP TABLE IF EXISTS rating;""")
    cursor.execute("""DROP TABLE IF EXISTS usertab;""")
    conn.commit() # <--- makes sure the change is shown in the database
    #rows = cursor.fetchall()
    #print(rows)
    cursor.close()
    conn.close()
    print("Done deleting tables")
