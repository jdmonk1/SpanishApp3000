import psycopg2
from codecs import encode

def start():
    try:
        connect_str = "dbname='spanish' user='postgres' host='localhost' port='5439'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cursor.execute("""SELECT form_2p FROM FlashcardsVerbs;""")
        conn.commit() # <--- makes sure the change is shown in the database
        rows = cursor.fetchall()
        print(encode(str.encode(rows[1][0]), 'hex'))
        hexstr = encode(str.encode(rows[614][0]), 'hex')
        print("hexstr[0] = ", hexstr[0])
        charlist = [[0xc3,0x83,0xc2,0x89],[0xc3,0x83,0xc2,0xad],[0xc3,0x83,0xc2,0xb3],[0xc3,0x83,0xc2,0xa1],[0xc3,0x83,0xc2,0xba],[0xc3,0x83,0xc5,0x92]]
        newcharlist = [[0xc3,0x19],[0xc3,0xad],[0xc3,0xb3],[0xc3,0xa1],[0xc3,0xba],[0xc3,0xbc]]
        for i in charlist:
            count = 0
            for k in range(2,(len(hexstr)-3),2):
                val = str(hexstr[k]) + str(hexstr([k+1]))
                if i[count] == int(val, 16):
                    count = count + 1
                else:
                    if i[0] == int(val, 16):
                        count = 1
                    else:
                        count = 0
                if count == 4:
                    hexstr[k-7:k-3] = newcharlist[i][0]
                    hexstr[k-5:k-2] = newcharlist[i][1]
                    count = 0
        print("hexstr = ", hexstr)
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        print("failed to test database")
        print(e)
