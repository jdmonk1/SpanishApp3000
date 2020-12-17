import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def start():
    try:
        #connect_str = "dbname='postgres' user='postgres' host='localhost' port='5439'"
        print("connect")
        connect_str = "user='postgres' host='localhost' port='5439'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        print("conected")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        print("autocommit")
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        
        cursor.execute("DROP DATABASE IF EXISTS spanish;")
        cursor.execute("CREATE DATABASE Spanish WITH ENCODING 'LATIN9' LC_COLLATE='C' LC_CTYPE='C' TEMPLATE=template0;")
        #conn.commit()
        cursor.close()
        conn.close()
        print("created Spanish Database!!")
        
        
        connect_str2 = "dbname='spanish' user='postgres' host='localhost' port='5439'"
        conn = psycopg2.connect(connect_str2)
        cursor = conn.cursor()
        print("conected to Spanish Database!!")
        # create a new table with a single column called "name"
        print("connected")
        print("create userTab")
        cursor.execute("""CREATE TABLE userTab(
            name text,
            password text,
            userTabID text,
            PRIMARY KEY (userTabID)
        );""")
        print("finshed")
        print("create listTemp")
        cursor.execute("""CREATE TABLE listTemp(
            FlashcardsVerbsID text,
            infinitive text,
            infinitive_english text,
            mood text,
            mood_english text,
            tense text,
            tense_english text,
            verb_english text,
            form_1s text,
            form_2s text,
            form_3s text,
            form_1p text,
            form_2p text,
            form_3p text,
            gerund text,
            gerund_english text,
            pastparticiple text,
            pastparticiple_english text,
            listTempID text,
            PRIMARY KEY (listTempID)
        );""")
        print("finshed")
        print("create FlashcardVerbs")
        cursor.execute("""CREATE TABLE FlashcardsVerbs(
            FlashcardsVerbsID text,
            infinitive text,
            infinitive_english text,
            mood text,
            mood_english text,
            tense text,
            tense_english text,
            verb_english text,
            form_1s text,
            form_2s text,
            form_3s text,
            form_1p text,
            form_2p text,
            form_3p text,
            gerund text,
            gerund_english text,
            pastparticiple text,
            pastparticiple_english text,
            PRIMARY KEY (FlashcardsVerbsID)
        );""")
        print("finshed")
        print("create Rating")
        cursor.execute("""CREATE TABLE Rating(
            wrong text,
            low text,
            medium text,
            high text,
            userRating text,
            RatingID text,
            PRIMARY KEY (RatingID)
        );""")
        print("finshed")
        print("create accuracyFreqency")
        cursor.execute("""CREATE TABLE accuracyFreqency(
            trysPerWord text,
            succesessPerWord text,
            failuresPerWord text,
            avgSuccesessPerWord decimal,
            leastMissedTensePerWord text,
            mostMissedTensePerWord text,
            avgMissedTensePerWord decimal,
            accuracyFreqencyID text,
            PRIMARY KEY (accuracyFreqencyID)
        );""")
        print("finshed")
        print("create FlashcardStats")
        cursor.execute("""CREATE TABLE FlashcardStats(
            accuracyFrequencyID text,
            avgSuccesessOverall decimal,
            leastMissedTenseOverall text,
            mostMissedTenseOverall text,
            avgMissedTenseOverall decimal,
            accuracyFreqencyID text,
            FlashcardsVerbsID text,
            FlashcardStatsID text,
            PRIMARY KEY (FlashcardStatsID, FlashcardsVerbsID, accuracyFreqencyID)
        );""")
        print("finshed")
        print("create Rated")
        cursor.execute("""CREATE TABLE Rated(
        RatingID text,
        FlashcardsVerbsID text,
        RatedID text,
        PRIMARY KEY (RatedID, RatingID, FlashcardsVerbsID));""")
        print("finshed")
        print("create Profile")
        cursor.execute("""CREATE TABLE Profile(
            RatedID text,
            FlashcardStatsID text,
            listTempID text,
            userTabID text,
            PRIMARY KEY (RatedID, userTabID, listTempID, FlashcardStatsID)
        );""")
        print("finshed")
        # run a SELECT statement - no data in there, but we can try it
        #cursor.execute("""SELECT * from tutorials""")
        conn.commit() # <--- makes sure the change is shown in the database
        print("commited!!")
        # rows = cursor.fetchall()
        # print(rows)
        cursor.close()
        conn.close()
        print("conection closed")
    except Exception as e:
        cursor.close()
        conn.close()
        print("Uh oh, can't connect. Invalid dbname, user password?")
        print(e)
