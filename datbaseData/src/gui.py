from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import random
import matplotlib.pyplot as plt
#import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.pyplot import figure
import PySimpleGUI as sg
import sql
#imports for database init
import subprocess
import psycopg2
import os
import sys
import apptest
import createDatabase
import fillDatabase
import removeDatabase
import testinsert
from tabs.library import LibraryTab
from tabs.update import UpdateTab
# from tabs.login import LoginTab
# from tabs.rating import RatingTab
from tabs.rounds import RoundsTab
# from tabs.stats import StatsTab

#db = sql.Database()  # import db
# lt = LibraryTab(db)
# lot = LoginTab(db)
# rt = RatingTab(db)
# rot = RoundsTab(db)
# st = StatsTab(db)


events = []
#st.addEvents(events)
mainWindowSize = (1500, 650)

def encodeList(itemsList, thing):
    itemsListNew = []
    for x in itemsList:
        b = []
        for y in x:
            if y is not None:
                pass
            else:
                b.append(None)
        tuple(b)
        itemsListNew.append(b)
    print(itemsListNew)
    return itemsListNew

def setup():
    print("start setup")
    d = subprocess.call([r'C:\datbaseData\src\postgresql-13.1-1-windows-x64-binaries2\pgsql\setup.bat'])
    print("complete setup")

def close():
    d = subprocess.call([r'C:\datbaseData\src\postgresql-13.1-1-windows-x64-binaries2\pgsql\close.bat'])

def initdbinfo():
    print("0")
    setup()
    print("1")
    try:
        createDatabase.start()
    except:
        print("database Setup")
    print("2")
    try:
        fillDatabase.start()
    except:
        print("database filled")
    print("3")
    #removeDatabase.start()
    print("4")
    testinsert.start()
    print("5")
    close()
    print("6")
    apptest.method()

def popupGUI(message):
    layout = [[sg.Text(message)],
                [sg.Button('OK', bind_return_key=True)]]
    window = sg.Window('WARNING', layout, font=("Roboto", 12), size=(450, 75), finalize=True)
    return window

class GUI:
    def __init__(self, db):
       self.Verbs = db.getALLVerbs()
       self.ListTmp = db.getListTmp()
       self.searchTmpList = db.getALLVerbs()
       self.confidenceLevel = 3
       self.score = 0
       self.VerbNumOnList = 1
       self.VerbNumOnListIndex = 1
       self.roundNum = 1
       self.TabKeys = ['tabgroupSearch', 'tabgroup']
       self.updateWindow = None
       self.updateItem = ()

    def updateTables(self, db):
        self.Verbs = db.getALLVerbs()
        self.ListTmp = db.getListTmp()
        #self.searchTmpList = db.getALLVerbs()

def create_window(lt, rt, score):
    plt.close('all')
    # main layout this contains everything
    layout = [[
        sg.TabGroup(
            [[
                lt.libraryTabGUI(),
                rt.RoundsTabGUI(score),
                sg.Tab('Theme', [[sg.Listbox(values=sg.theme_list(), key='-THEME-LIST-', size=(20, 200), enable_events=True), sg.Button('SAVE NEW THEME', key='-THEME-BUTTON-')]], key='-THEME-TAB-'),
            ]],
            key='tabgroup',
            enable_events=True
        )  # end of TabGroup

    ]
    ]  # end of layout

    # Create the window
    window = sg.Window('SpanishApp3000', layout, font=(
        "Roboto", 12), size=mainWindowSize, finalize=True, element_justification='c')
        
    return window

def main(conn, cursor):
    plt.close('all')
    sg.theme('Dark Grey 9')  # set window theme
    db = sql.Database(conn, cursor)
    gui = GUI(db)
    result = db.getAllFlashcardsVerbsID()
    print(result)
    lt = LibraryTab(db)
    ut = UpdateTab(db)
    rt = RoundsTab(db)
    
    

    window = create_window(lt, rt, gui.score)

    def isValid(*args):
        for elem in args:
            if elem == '':
                return False
        return True

    def updatelibtabs(db):
        plt.close('all')
        gui.updateTables(db)
        
        
        window['-TABLE-L01-'].update(values=gui.Verbs)
        window['-TABLE-L02-'].update(values=gui.ListTmp)
        window['-TABLE2-L02-'].update(values=gui.searchTmpList)

    def updateSearchTabs(inputValues):
        plt.close('all')
        #gui.searchTmpList = db.getSearchedVerbs()
        

    def checkButtonPress(event, values):
        pass
        ### START BUTTONS ###
        
        if event == '-START-BUTTON-L02-':
            try:
                print("got here1")
                gui.VerbNumOnList = gui.ListTmp[values['-TABLE-L02-'][0]]
                gui.VerbNumOnListIndex = values['-TABLE-L02-'][0]
                print("got here")

                
                if gui.roundNum == 21:
                    gui.roundNum = 1
                    gui.score = 0
                
                gui.updateWindow = sg.Window('Round ' + str(gui.roundNum) + 'Verb# ' + str(gui.VerbNumOnListIndex + 1), rt.startRoundsGUI(gui.VerbNumOnList), font=("Roboto", 12), size=(1000, 500), finalize=True)
                gui.confidenceLevel = 3

                button, updateValues = gui.updateWindow.read()
                if button == 'NEXT':
                    print("at begining")
                    VerbInfinitiveToUpdate = updateValues['-INFINITIVE-L02-']
                    print("past one!")
                    VerbMood_englishToUpdate = updateValues['-MOOD_ENGLISH-L02-']
                    VerbTense_englishToUpdate = updateValues['-TENSE_ENGLISH-L02-']
                    print("past 3!")
                    VerbForm_1sToUpdate = updateValues['-FORM_1S-L02-']
                    VerbForm_2sToUpdate = updateValues['-FORM_2S-L02-']
                    VerbForm_3sToUpdate = updateValues['-FORM_3S-L02-']
                    VerbForm_1pToUpdate = updateValues['-FORM_1P-L02-']
                    VerbForm_2pToUpdate = updateValues['-FORM_2P-L02-']
                    VerbForm_3pToUpdate = updateValues['-FORM_3P-L02-']
                    VerbGerundToUpdate = updateValues['-GERUND-L02-']
                    VerbPastparticipleToUpdate = updateValues['-PASTPARTICIPLE-L02-']
                    VerbConfidenceValue = updateValues['-CONFIDENCE-L02-']
                    print("got values!")
                    OldInfinitive = 1
                    oldmood_english = 2
                    oldtense_english = 3
                    print("num on list = ", gui.VerbNumOnList)
                    print("num on list index = ", gui.VerbNumOnListIndex)
                    print("going to db.updateVerb")
                    j = gui.VerbNumOnListIndex
                    result1 = db.checkVerb(j,VerbInfinitiveToUpdate,VerbMood_englishToUpdate,VerbTense_englishToUpdate,VerbForm_1sToUpdate,VerbForm_2sToUpdate,VerbForm_3sToUpdate,VerbForm_1pToUpdate,VerbForm_2pToUpdate,VerbForm_3pToUpdate,VerbGerundToUpdate,VerbPastparticipleToUpdate,OldInfinitive,oldmood_english,oldtense_english)
                    print("Result1 = ", result1) 
                    try:
                        if VerbConfidenceValue == 'Wrong 0':
                            gui.confidenceLevel = 0
                        elif VerbConfidenceValue == 'High 3':
                            gui.confidenceLevel = 3
                        elif VerbConfidenceValue == 'Medium 2':
                            gui.confidenceLevel = 2
                        elif VerbConfidenceValue == 'Low 1':
                            gui.confidenceLevel = 1
                    except Exception as e:
                        print(e)
                    
                    if result1 == True and gui.confidenceLevel == 3:
                        gui.score += 3
                    if result1 == True and gui.confidenceLevel == 2:
                        gui.score += 2
                    if result1 == True and gui.confidenceLevel == 1:
                        gui.score += 1
                    if result1 == True and gui.confidenceLevel == 0:
                        gui.score += 0
                    if result1 == False and gui.confidenceLevel == 3:
                        gui.score -= 3
                    if result1 == False and gui.confidenceLevel == 2:
                        gui.score -= 2
                    if result1 == False and gui.confidenceLevel == 1:
                        gui.score -= 1
                    if result1 == False and gui.confidenceLevel == 0:
                        gui.score -= 0
                    print("score = ", gui.score)
                    print("going to update")
                    updatelibtabs(db)
                    updateSearchTabs(values)
                    print("Done updating")
                    gui.roundNum += 1
                    gui.updateWindow.close()
                    # plt.close('all')
                    # window.close()
                    # window = create_window(lt, rt, gui.score)
                if button == 'CANCEL':
                    gui.updateWindow.close()
            except Exception as e:
                print(e)
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()
        
        if event == '-UPDATE-QUESTION-BUTTON-L02-':
            try:
                print("got here1")
                #gui.VerbNumOnList = gui.ListTmp[values['-TABLE-L02-'][0]]
                #gui.VerbNumOnListIndex = values['-TABLE-L02-'][0]
                print("got here")

                
                # if gui.roundNum == 21:
                    # gui.roundNum = 1
                    # gui.score = 0
                
                # gui.updateWindow = sg.Window('Round ' + str(gui.roundNum) + 'Verb# ' + str(gui.VerbNumOnListIndex + 1), rt.startRoundsGUI(gui.VerbNumOnList), font=("Roboto", 12), size=(1000, 500), finalize=True)
                # gui.confidenceLevel = 3

                #button, updateValues = gui.updateWindow.read()
                updateValuesInfinitive = values['-INFINITIVELIST-L02-']
                updateValuesMoodEnglish = values['-MOODLIST-L02-']
                updateValuesTenseEnglish = values['-TENSELIST-L02-']
                updateValuesQuestionNumber = values['-QUESTIONLIST-L02-']
                print("at begining")
                print("got values!")
                #print("num on list = ", gui.VerbNumOnList)
                #print("num on list index = ", gui.VerbNumOnListIndex)
                print("going to db.updateListTmp")
                j = str(int(updateValuesQuestionNumber) - 1)
                t = db.updateListTmpChoice(j,updateValuesInfinitive,updateValuesMoodEnglish,updateValuesTenseEnglish)
                #print("Result1 = ", result1) 
                
                print("score = ", gui.score)
                print("going to update")
                updatelibtabs(db)
                updateSearchTabs(values)
                print("Done updating")
                #gui.updateWindow.close()
                # plt.close('all')
                # window.close()
                # window = create_window(lt, rt, gui.score)
            except Exception as e:
                print(e)
                popup = popupGUI('Please select Values to update questions!')
                button, values = popup.read()
                popup.close()

        if event == '-UPDATE-RANDOM-QUESTION-BUTTON-L02-':
            try:
                print("got here1")
                #gui.VerbNumOnList = gui.ListTmp[values['-TABLE-L02-'][0]]
                #gui.VerbNumOnListIndex = values['-TABLE-L02-'][0]
                print("got here")

                
                # if gui.roundNum == 21:
                    # gui.roundNum = 1
                    # gui.score = 0
                
                # gui.updateWindow = sg.Window('Round ' + str(gui.roundNum) + 'Verb# ' + str(gui.VerbNumOnListIndex + 1), rt.startRoundsGUI(gui.VerbNumOnList), font=("Roboto", 12), size=(1000, 500), finalize=True)
                # gui.confidenceLevel = 3
                listofchoices = []
                for j in range(20):
                    listofchoices.append(gui.ListTmp[j][0])
                #button, updateValues = gui.updateWindow.read()
                for i in range(20):
                    randomint1 = random.randint(1,11466)
                    
                    print("at begining")
                    print("got values!")
                    #print("num on list = ", gui.VerbNumOnList)
                    #print("num on list index = ", gui.VerbNumOnListIndex)
                    print("going to db.updateListTmp")
                    #j = updateValuesQuestionNumber
                    if str(randomint1) in listofchoices:
                        pass
                    else:
                        listofchoices.append(str(randomint1))
                        t = db.updateListTmpChoiceRandom(randomint1, i)
                #print("Result1 = ", result1) 
                
                print("score = ", gui.score)
                print("going to update")
                updatelibtabs(db)
                updateSearchTabs(values)
                print("Done updating")
                #gui.updateWindow.close()
                # plt.close('all')
                # window.close()
                # window = create_window(lt, rt, gui.score)
            except Exception as e:
                print(e)
                popup = popupGUI('Please select Values to update questions!')
                button, values = popup.read()
                popup.close()

        if event == '-SEARCH-BUTTON-L02-':
            try:
                print("got here1")
                #gui.VerbNumOnList = gui.ListTmp[values['-TABLE-L02-'][0]]
                #gui.VerbNumOnListIndex = values['-TABLE-L02-'][0]
                print("got here")

                
                # if gui.roundNum == 21:
                    # gui.roundNum = 1
                    # gui.score = 0
                
                # gui.updateWindow = sg.Window('Round ' + str(gui.roundNum) + 'Verb# ' + str(gui.VerbNumOnListIndex + 1), rt.startRoundsGUI(gui.VerbNumOnList), font=("Roboto", 12), size=(1000, 500), finalize=True)
                # gui.confidenceLevel = 3
                searchQuerry = values['-SEARCH-INUPUT-L02-']
                print('got input')
                gui.searchTmpList = db.getSearchedVerbs(searchQuerry)
                print('searchQuerry sucessfull')
                #print("Result1 = ", result1) 
                window['-TABLE2-L02-'].update(values=gui.searchTmpList)
                print("score = ", gui.score)
                print("going to update")
                updatelibtabs(db)
                updateSearchTabs(values)
                print("Done updating")
                #gui.updateWindow.close()
                # plt.close('all')
                # window.close()
                # window = create_window(lt, rt, gui.score)
            except Exception as e:
                print(e)
                popup = popupGUI('Please select Values to update questions!')
                button, values = popup.read()
                popup.close()

        if event == '-UPDATE-SEARCH-BUTTON-L02-':
            try:
                print("got here1")
                gui.VerbNumOnList = gui.searchTmpList[values['-TABLE2-L02-'][0]]
                gui.VerbNumOnListIndex = values['-TABLE2-L02-'][0]
                print("got here")

                
                # if gui.roundNum == 21:
                    # gui.roundNum = 1
                    # gui.score = 0
                
                # gui.updateWindow = sg.Window('Round ' + str(gui.roundNum) + 'Verb# ' + str(gui.VerbNumOnListIndex + 1), rt.startRoundsGUI(gui.VerbNumOnList), font=("Roboto", 12), size=(1000, 500), finalize=True)
                # gui.confidenceLevel = 3

                #button, updateValues = gui.updateWindow.read()
                updateValuesInfinitive = gui.searchTmpList[gui.VerbNumOnListIndex][0]
                updateValuesMoodEnglish = gui.searchTmpList[gui.VerbNumOnListIndex][1]
                updateValuesTenseEnglish = gui.searchTmpList[gui.VerbNumOnListIndex][2]
                updateValuesQuestionNumber = values['-QUESTIONLIST2-L02-']
                print("at begining")
                print("got values!")
                #print("num on list = ", gui.VerbNumOnList)
                #print("num on list index = ", gui.VerbNumOnListIndex)
                print("going to db.updateListTmp")
                j = int(updateValuesQuestionNumber)
                t = db.updateListTmpChoice(j,updateValuesInfinitive,updateValuesMoodEnglish,updateValuesTenseEnglish)
                #print("Result1 = ", result1) 
                
                print("score = ", gui.score)
                print("going to update")
                updatelibtabs(db)
                updateSearchTabs(values)
                print("Done updating")
                #gui.updateWindow.close()
                # plt.close('all')
                # window.close()
                # window = create_window(lt, rt, gui.score)
            except Exception as e:
                print(e)
                popup = popupGUI('Please select Values to update questions!')
                button, values = popup.read()
                popup.close()

        ### SEARCH EVENTS ###

        ### DELETE SELECTED SEARCH ###

        # delete searched song

        # delete searched artist

        # delete searched album

        # delete searched musician

        # delete searched RecordLabel

        ### ADD EVENTS ###

        # ADD RECORD LABEL

        # ADD ARTIST

        # ADD Album

        # ADD SONG

        ### LIBRARY EVENTS ###

        # LIST SONGS - UPDATE RATING

        # DELETE SECTION

        # DELETE RECORD LABEL
        if event == '-DELETE-BUTTON-L01-':

            try:
                VerbIndex = values['-TABLE-L01-'][0]
                VerbInfinitiveToDelete = gui.Verbs[VerbIndex][0]
                #VerbInfinitive_englishToDelete = gui.Verbs[VerbIndex][1]
                #VerbMoodToDelete = gui.Verbs[VerbIndex][2]
                VerbMood_englishToDelete = gui.Verbs[VerbIndex][1]
                #VerbTenseToDelete = gui.Verbs[VerbIndex][4]
                VerbTense_englishToDelete = gui.Verbs[VerbIndex][2]
                #VerbVerb_englishToDelete = gui.Verbs[VerbIndex][6]
                VerbForm_1sToDelete = gui.Verbs[VerbIndex][3]
                VerbForm_2sToDelete = gui.Verbs[VerbIndex][4]
                VerbForm_3sToDelete = gui.Verbs[VerbIndex][5]
                VerbForm_1pToDelete = gui.Verbs[VerbIndex][6]
                VerbForm_2pToDelete = gui.Verbs[VerbIndex][7]
                VerbForm_3pToDelete = gui.Verbs[VerbIndex][8]
                VerbGerundToDelete = gui.Verbs[VerbIndex][9]
                #VerbGerund_englishToDelete = gui.Verbs[VerbIndex][14]
                VerbPastparticipleToDelete = gui.Verbs[VerbIndex][10]
                #VerbPastparticiple_englishToDelete = gui.Verbs[VerbIndex][15]


                db.deleteVerb(VerbInfinitiveToDelete,
                                    VerbMood_englishToDelete,
                                    VerbTense_englishToDelete,
                                    VerbForm_1sToDelete,
                                    VerbForm_2sToDelete,
                                    VerbForm_3sToDelete,
                                    VerbForm_1pToDelete,
                                    VerbForm_2pToDelete,
                                    VerbForm_3pToDelete,
                                    VerbGerundToDelete,
                                    VerbPastparticipleToDelete)

                updateSearchTabs(values)
            except:
                popup = popupGUI('Please select a Record to delete')
                button, values = popup.read()
                popup.close()

            updatelibtabs(db)

        # DELETE RECORD LABEL

        # DELETE ARTIST

        # DELETE ALBUM

        # DELETE SONG

        ### FEELING LUCKY EVENTS ###

        #### UPDATE EVENTS ####

        # UPDATE RECORD LABEL - LIBRARY TAB

        if event == '-UPDATE-BUTTON-L01-':
            try:
                print("got here1")
                gui.updateItem = gui.Verbs[values['-TABLE-L01-'][0]]
                print("got here")

                gui.updateWindow = sg.Window('Update Verb', ut.updateRecordLabelGUI(), font=("Roboto", 12), size=(1000, 500), finalize=True)

                button, updateValues = gui.updateWindow.read()
                if button == 'UPDATE':
                    print("at begining")
                    VerbInfinitiveToUpdate = updateValues['-INFINITIVE-U01-']
                    print("past one!")
                    VerbMood_englishToUpdate = updateValues['-MOOD_ENGLISH-U01-']
                    VerbTense_englishToUpdate = updateValues['-TENSE_ENGLISH-U01-']
                    print("past 3!")
                    VerbForm_1sToUpdate = updateValues['-FORM_1S-U01-']
                    VerbForm_2sToUpdate = updateValues['-FORM_2S-U01-']
                    VerbForm_3sToUpdate = updateValues['-FORM_3S-U01-']
                    VerbForm_1pToUpdate = updateValues['-FORM_1P-U01-']
                    VerbForm_2pToUpdate = updateValues['-FORM_2P-U01-']
                    VerbForm_3pToUpdate = updateValues['-FORM_3P-U01-']
                    VerbGerundToUpdate = updateValues['-GERUND-U01-']
                    VerbPastparticipleToUpdate = updateValues['-PASTPARTICIPLE-U01-']
                    print("got values!")
                    OldInfinitive = gui.updateItem[0]
                    oldmood_english = gui.updateItem[1]
                    oldtense_english = gui.updateItem[2]
                    print("going to db.updateVerb")
                    db.updateVerb(VerbInfinitiveToUpdate,VerbMood_englishToUpdate,VerbTense_englishToUpdate,VerbForm_1sToUpdate,VerbForm_2sToUpdate,VerbForm_3sToUpdate,VerbForm_1pToUpdate,VerbForm_2pToUpdate,VerbForm_3pToUpdate,VerbGerundToUpdate,VerbPastparticipleToUpdate,OldInfinitive,oldmood_english,oldtense_english)
                    print("going to update")
                    updatelibtabs(db)
                    updateSearchTabs(values)
                    print("Done updating")
                gui.updateWindow.close()

            except Exception as e:
                print(e)
                popup = popupGUI('Please select something to update')
                button, values = popup.read()
                popup.close()
        # UPDATE RECORD LABEL - SEARCH TAB

        # UPDATE ARTIST - LIBRARY TAB

        # UPDATE ARTIST - SEARCH TAB

        # UPDATE ALBUM - LIBRARY TAB

        # UPDATE ALBUM - SEARCH TAB

        # UPDATE SONG - LIBRARY TAB

        # UPDATE SONG - SEARCH TAB

    while True:

        event, values = window.read()

        if window is None:
            window = create_window(lt, rt, gui.score)

        ### THEME CHANGE ###

        if event == '-THEME-BUTTON-':
            try:
                sg.theme(values['-THEME-LIST-'][0])
                plt.close('all')
                window.close()
                window = create_window(lt, rt, gui.score)
            except:
                popup = popupGUI('Please select a theme')
                button, values = popup.read()
                popup.close()
        
        if event == '-REFRESH-BUTTON-L02-':
            try:
                plt.close('all')
                window.close()
                window = create_window(lt, rt, gui.score)
            except:
                popup = popupGUI('Please select a theme')
                button, values = popup.read()
                popup.close()
        
        if event == sg.WINDOW_CLOSED:
            break

        checkButtonPress(event, values)

    # close the program
    print("6")
    window.close()


if __name__ == '__main__':
    print("Seting up Database......")
    setup()
    print("Done")
    #print("1")
    #removeDatabase.start()
    #try:
    #    createDatabase.start()
    #except:
    #    print("database Setup")
    #print("2")
    #try:
    #    fillDatabase.start()
    #except:
    #    print("database filled")
    #print("3")
    #try:
    #    testinsert.start()
    #except Exception as e:
    #    print(e)
    #print("4")
    #apptest.method()
    connect_str = "dbname='spanish' user='postgres' host='localhost' port='5439'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    main(conn, cursor)
    #removeDatabase.start()
    #print("5")
    cursor.close()
    conn.close()
    print("Closing and disconecting.....")
    close()
    print("Disconected")
