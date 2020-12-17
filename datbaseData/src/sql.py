import random
from random import randint
import time
import psycopg2
from string import Template
from psycopg2 import OperationalError

# Database
class Database:
    # init
    
    def setup():
        print("start setup")
        d = subprocess.call([r'C:\datbaseData\src\postgresql-13.1-1-windows-x64-binaries\pgsql\setup.bat'])
        print("complete setup")
        return d

    def close():
        d = subprocess.call([r'C:\datbaseData\src\postgresql-13.1-1-windows-x64-binaries\pgsql\close.bat'])
        
    def __init__(self, conn, cursor):
        #self.userName = getpass.getuser()
        # connect_str = "dbname='postgres' user='postgres' host='localhost' port='5439'"
        # self.conn = psycopg2.connect(connect_str)
        # self.conn.autocommit = True
        # self.cur = self.conn.cursor()
        self.conn = conn
        self.cur = cursor
        self.conn.autocommit = True

    # exit
    def closeConnection(self):
        self.cur.close()
        self.conn.close()

    # getting items from the list
    def getItems(self):
        result = []
        for i in self.cur:
            result.append(i)
        return result

    # getting items from the list subscripted
    def getSubscriptedItems(self):
        result = []
        for i in self.cur:
            i = i[0]
            result.append(i)
        return result

    # replace apostrophe for edge cases
    def replaceApostrophe(self, myString):
        myString = myString.replace("'", "")
        # myString = re.sub('(?<=[a-z])\'(?=[a-z])', '', myString)
        return myString

    def getAllFlashcardsVerbsID(self):
        result = []
        self.cur.execute("""SELECT FlashcardsVerbsID FROM FlashcardsVerbs;""")
        return self.getItems()
        
    def getALLVerbs(self):
        result = []
        self.cur.execute("SELECT infinitive, mood_english, tense_english, form_1s ,form_2s ,form_3s ,form_1p ,form_2p ,form_3p ,gerund, pastparticiple FROM Profile P, Rated R, FlashcardsVerbs V WHERE P.RatedID = R.RatedID AND R.RatedID = V.FlashcardsVerbsID ORDER BY LOWER(infinitive)")
        return self.getItems()
        
    def deleteVerb(self, VerbInfinitiveToDelete,VerbMood_englishToDelete,VerbTense_englishToDelete,VerbForm_1sToDelete,VerbForm_2sToDelete,VerbForm_3sToDelete,VerbForm_1pToDelete,VerbForm_2pToDelete,VerbForm_3pToDelete,VerbGerundToDelete,VerbPastparticipleToDelete):
        try:
            self.cur.execute("SELECT V.FlashcardsVerbsID FROM Profile P, Rated R, FlashcardsVerbs V WHERE P.RatedID = R.RatedID AND R.RatedID = V.FlashcardsVerbsID AND LOWER(V.infinitive) = '%s'AND LOWER(V.Mood_english) = '%s' AND LOWER(V.Tense_english) = '%s' AND LOWER(V.Form_1s) = '%s' AND LOWER(V.Form_2s) = '%s' AND LOWER(V.Form_3s) = '%s' AND LOWER(V.Form_1p) = '%s' AND LOWER(V.Form_2p) = '%s' AND LOWER(V.Form_3p) = '%s' AND LOWER(V.Gerund) = '%s' AND LOWER(V.Pastparticiple) = '%s'" % (VerbInfinitiveToDelete.lower(),VerbMood_englishToDelete.lower(),VerbTense_englishToDelete.lower(),VerbForm_1sToDelete.lower(),VerbForm_2sToDelete.lower(),VerbForm_3sToDelete.lower(),VerbForm_1pToDelete.lower(),VerbForm_2pToDelete.lower(),VerbForm_3pToDelete.lower(),VerbGerundToDelete.lower(),VerbPastparticipleToDelete.lower()))
            universalID = self.getItems()[0][0]
            self.cur.execute("DELETE FROM Profile WHERE RatedID = '%s'" % (universalID))
            self.cur.execute("DELETE FROM Rated WHERE RatedID = '%s' AND FlashcardsVerbsID = '%s'" % (universalID, universalID))
            self.cur.execute("DELETE FROM FlashcardsVerbs WHERE FlashcardsVerbsID = '%s'" % (universalID))
        except Exception as e:
            print("sql.py deleteVerb")
            print(e)

    def updateVerb(self, VerbInfinitiveToUpdate,
                    VerbMood_englishToUpdate,
                    VerbTense_englishToUpdate,
                    VerbForm_1sToUpdate,
                    VerbForm_2sToUpdate,
                    VerbForm_3sToUpdate,
                    VerbForm_1pToUpdate,
                    VerbForm_2pToUpdate,
                    VerbForm_3pToUpdate,
                    VerbGerundToUpdate,
                    VerbPastparticipleToUpdate,
                    OldInfinitive,
                    oldmood_english,
                    oldtense_english):
        try:
            self.cur.execute("UPDATE FlashcardsVerbs SET Infinitive = '%s', Mood_english = '%s' , Tense_english = '%s', Form_1s = '%s', Form_2s = '%s', Form_3s = '%s', Form_1p = '%s', Form_2p = '%s', Form_3p = '%s', Gerund = '%s', Pastparticiple = '%s' WHERE infinitive = '%s' AND mood_english = '%s' AND tense_english = '%s'" % (self.replaceApostrophe(VerbInfinitiveToUpdate),self.replaceApostrophe(VerbMood_englishToUpdate),self.replaceApostrophe(VerbTense_englishToUpdate),self.replaceApostrophe(VerbForm_1sToUpdate),self.replaceApostrophe(VerbForm_2sToUpdate),self.replaceApostrophe(VerbForm_3sToUpdate),self.replaceApostrophe(VerbForm_1pToUpdate),self.replaceApostrophe(VerbForm_2pToUpdate),self.replaceApostrophe(VerbForm_3pToUpdate),self.replaceApostrophe(VerbGerundToUpdate),self.replaceApostrophe(VerbPastparticipleToUpdate),OldInfinitive,oldmood_english,oldtense_english))
            self.conn.commit()
        except Exception as e:
            print(e)

    def getListTmp(self):
        result = []
        self.cur.execute("SELECT L.infinitive, L.mood_english, L.tense_english FROM ListTemp L ORDER BY LOWER(L.ListTempID)")
        return self.getItems()
        
    def getListTmpTense(self, i):
        result = []
        self.cur.execute("SELECT L.Infinitive, L.Mood_english, L.Tense_english, L.Form_1s, L.Form_2s, L.Form_3s, L.Form_1p, L.Form_2p, L.Form_3p, L.Gerund, L.Pastparticiple FROM ListTemp L WHERE L.FlashcardsVerbsID = '%s' ORDER BY LOWER(Tense)" % (i))
        return self.getItems()
    def checkVerb(self, i, VerbInfinitiveToUpdate,
                    VerbMood_englishToUpdate,
                    VerbTense_englishToUpdate,
                    VerbForm_1sToUpdate,
                    VerbForm_2sToUpdate,
                    VerbForm_3sToUpdate,
                    VerbForm_1pToUpdate,
                    VerbForm_2pToUpdate,
                    VerbForm_3pToUpdate,
                    VerbGerundToUpdate,
                    VerbPastparticipleToUpdate,
                    OldInfinitive,
                    oldmood_english,
                    oldtense_english):
        try:
            self.cur.execute("SELECT T.FlashcardsVerbsID FROM ListTemp T WHERE Infinitive = '%s' AND Mood_english = '%s' AND Tense_english = '%s' AND Form_1s = '%s' AND Form_2s = '%s' AND Form_3s = '%s' AND Form_1p = '%s' AND Form_2p = '%s' AND Form_3p = '%s' AND Gerund = '%s' AND Pastparticiple = '%s'" % (self.replaceApostrophe(VerbInfinitiveToUpdate),self.replaceApostrophe(VerbMood_englishToUpdate),self.replaceApostrophe(VerbTense_englishToUpdate),self.replaceApostrophe(VerbForm_1sToUpdate),self.replaceApostrophe(VerbForm_2sToUpdate),self.replaceApostrophe(VerbForm_3sToUpdate),self.replaceApostrophe(VerbForm_1pToUpdate),self.replaceApostrophe(VerbForm_2pToUpdate),self.replaceApostrophe(VerbForm_3pToUpdate),self.replaceApostrophe(VerbGerundToUpdate),self.replaceApostrophe(VerbPastparticipleToUpdate)))
            universalID = self.getItems()
            print("universalID = ", universalID)
            print(self.getListTmpTense(str(i)))
            print("len(universalID) = ", len(universalID))
            if len(universalID) == 0:
                return False
            else:
                universalID = universalID[0][0]
                if universalID == str(i):
                    #self.conn.commit()
                    return True
                else:
                    #self.conn.commit()
                    return False
        except Exception as e:
            print(e)

    def FindVerbList(self):
        result = []
        self.cur.execute("SELECT DISTINCT F.infinitive FROM FlashcardsVerbs F ORDER BY F.infinitive")
        items = self.getItems()
        print('items = ', items)
        itemsList = []
        for i in items:
            print("i = ", i)
            print("i[0] = ", i[0])
            str1 = ''.join(i[0])
            itemsList.append(str1)
        return itemsList

    def updateListTmpChoice(self,index,updateValuesInfinitive,updateValuesMoodEnglish,updateValuesTenseEnglish):
        Result = []
        self.cur.execute("SELECT * FROM FlashcardsVerbs F WHERE LOWER(infinitive) = '%s' AND LOWER(mood_english) = '%s' AND LOWER(tense_english) = '%s'" % (updateValuesInfinitive.lower(),updateValuesMoodEnglish.lower(),updateValuesTenseEnglish.lower()))
        print("step 1")
        universalresults = self.getItems()
        print(universalresults)
        universalresults2 = []
        for items in universalresults:
            for i in range(18):
                print(type(None))
                print(type(items[i]))
                if items[i] is None:
                    universalresults2.append('NoItem')
                else:
                    universalresults2.append(items[i])
        universalresults = [tuple(universalresults2)]
        universalID = universalresults[0][0]
        universalinfinitive = universalresults[0][1]
        universalinfinitive_english = universalresults[0][2]
        universalmood = universalresults[0][3]
        universalmood_english = universalresults[0][4]
        universaltesnse = universalresults[0][5]
        universaltense_english = universalresults[0][6]
        universalverb_english = universalresults[0][7]
        universalform_1s = universalresults[0][8]
        universalform_2s = universalresults[0][9]
        universalform_3s = universalresults[0][10]
        universalform_1p = universalresults[0][11]
        universalform_2p = universalresults[0][12]
        universalform_3p = universalresults[0][13]
        universalgerund = universalresults[0][14]
        universalgerund_english = universalresults[0][15]
        universalpastparticiple = universalresults[0][16]
        universalpastparticiple_english = universalresults[0][17]
        print("step 2")
        #universallistTempID = universalresults[0][18]
        print("step 3")
        self.cur.execute("DELETE FROM ListTemp WHERE ListTempID = '%s'" % (str(index)))
        print("step 4")
        self.cur.execute("INSERT INTO ListTemp(FlashcardsVerbsID, infinitive, infinitive_english ,mood ,mood_english ,tense ,tense_english ,verb_english ,form_1s ,form_2s ,form_3s ,form_1p ,form_2p ,form_3p ,gerund ,gerund_english ,pastparticiple ,pastparticiple_english, listTempID) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (universalID, self.replaceApostrophe(universalinfinitive), self.replaceApostrophe(universalinfinitive_english), self.replaceApostrophe(universalmood), self.replaceApostrophe(universalmood_english), self.replaceApostrophe(universaltesnse), self.replaceApostrophe(universaltense_english), self.replaceApostrophe(universalverb_english), self.replaceApostrophe(universalform_1s), self.replaceApostrophe(universalform_2s), self.replaceApostrophe(universalform_3s), self.replaceApostrophe(universalform_1p), self.replaceApostrophe(universalform_2p), self.replaceApostrophe(universalform_3p), self.replaceApostrophe(universalgerund), self.replaceApostrophe(universalgerund_english), self.replaceApostrophe(universalpastparticiple), self.replaceApostrophe(universalpastparticiple_english), str(index)))
        print("step 5")

    def updateListTmpChoiceRandom(self,index,questionNum):
        Result = []
        self.cur.execute("SELECT * FROM FlashcardsVerbs F WHERE F.FlashcardsVerbsID = '%s'" % (str(index)))
        print("step 1")
        universalresults = self.getItems()
        print(universalresults)
        universalresults2 = []
        for items in universalresults:
            for i in range(18):
                print(type(None))
                print(type(items[i]))
                if items[i] is None:
                    universalresults2.append('NoItem')
                else:
                    universalresults2.append(items[i])
        universalresults = [tuple(universalresults2)]    
        universalID = universalresults[0][0]
        universalinfinitive = universalresults[0][1]
        universalinfinitive_english = universalresults[0][2]
        universalmood = universalresults[0][3]
        universalmood_english = universalresults[0][4]
        universaltesnse = universalresults[0][5]
        universaltense_english = universalresults[0][6]
        universalverb_english = universalresults[0][7]
        universalform_1s = universalresults[0][8]
        universalform_2s = universalresults[0][9]
        universalform_3s = universalresults[0][10]
        universalform_1p = universalresults[0][11]
        universalform_2p = universalresults[0][12]
        universalform_3p = universalresults[0][13]
        universalgerund = universalresults[0][14]
        universalgerund_english = universalresults[0][15]
        universalpastparticiple = universalresults[0][16]
        universalpastparticiple_english = universalresults[0][17]
        print("step 2")
        #universallistTempID = universalresults[0][18]
        print("step 3")
        self.cur.execute("DELETE FROM ListTemp WHERE ListTempID = '%s'" % (str(questionNum)))
        print("step 4")
        self.cur.execute("INSERT INTO ListTemp(FlashcardsVerbsID, infinitive, infinitive_english ,mood ,mood_english ,tense ,tense_english ,verb_english ,form_1s ,form_2s ,form_3s ,form_1p ,form_2p ,form_3p ,gerund ,gerund_english ,pastparticiple ,pastparticiple_english, listTempID) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (universalID, self.replaceApostrophe(universalinfinitive), self.replaceApostrophe(universalinfinitive_english), self.replaceApostrophe(universalmood), self.replaceApostrophe(universalmood_english), self.replaceApostrophe(universaltesnse), self.replaceApostrophe(universaltense_english), self.replaceApostrophe(universalverb_english), self.replaceApostrophe(universalform_1s), self.replaceApostrophe(universalform_2s), self.replaceApostrophe(universalform_3s), self.replaceApostrophe(universalform_1p), self.replaceApostrophe(universalform_2p), self.replaceApostrophe(universalform_3p), self.replaceApostrophe(universalgerund), self.replaceApostrophe(universalgerund_english), self.replaceApostrophe(universalpastparticiple), self.replaceApostrophe(universalpastparticiple_english), str(questionNum)))
        print("step 5")

    def getSearchedVerbs(self, searchQuerry):
        searchQuerry = searchQuerry + '%'
        result = []
        self.cur.execute("SELECT F.infinitive, F.mood_english, F.tense_english, F.form_1s ,F.form_2s ,F.form_3s ,F.form_1p ,F.form_2p ,F.form_3p ,F.gerund, F.pastparticiple FROM FlashcardsVerbs F WHERE LOWER(F.infinitive) LIKE '%s' ORDER BY LOWER(F.infinitive)" % (self.replaceApostrophe(searchQuerry.lower())))
        return self.getItems()