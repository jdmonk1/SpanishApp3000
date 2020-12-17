import psycopg2

def start():
    try:
        connect_str = "dbname='postgres' user='postgres' host='localhost' port='5439'"
        connect_str2 ="dbname='spanish' user='postgres' host='localhost' port='5439'" 
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str2)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cursor.execute("""COPY flashcardsVerbs FROM 'C:/datbaseData/src/jehle_verb_database.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY flashcardStats FROM 'C:/datbaseData/src/FlashcardStats.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY accuracyFreqency FROM 'C:/datbaseData/src/accuracyFrequency.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY listTemp FROM 'C:/datbaseData/src/ListTemp.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY Profile FROM 'C:/datbaseData/src/Profile.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY Rated FROM 'C:/datbaseData/src/Rated.csv' DELIMITER ',' CSV;""")
        cursor.execute("""COPY Rating FROM 'C:/datbaseData/src/Rating.csv' DELIMITER ',' CSV;""")
        conn.commit() # <--- makes sure the change is shown in the database
        print("comitt fill database")
        # rows = cursor.fetchall()
        # print(rows)
        cursor.close()
        conn.close()
        print("conection closed")
    except Exception as e:
        cursor.close()
        conn.close()
        print("failed to fill database")
        print(e)
