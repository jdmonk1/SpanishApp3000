import PySimpleGUI as sg

### #### #### #### #### #### #### #### #### ###
#               START OF LIB TABS             #
### #### #### #### #### #### #### #### #### ###
class RoundsTab:
    def __init__(self, db):
        self.db = db
        self.TenseList = ['Future Perfect', 'Past Perfect', 'Conditional', 'Future Perfect', 'Preterite', 'Future', 'Present Perfect', 'Conditional Perfect', 'Imperfect', 'Present', 'Past Perfect', 'Preterite (Archaic)']
        self.ConfidenceList = ['High 3', 'Medium 2', 'Low 1', 'Wrong 0']
        self.MoodList = ['Imperative Affirmative', 'Imperative Negative', 'Indicative', 'Subjunctive']
        self.QuestionList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        thing1 = db.FindVerbList()
        self.InfinitiveList = thing1
        print(self.InfinitiveList)
    
    def encodeList(self, itemsList):
        itemsListNew = []
        for x in itemsList:
            b = []
            for y in x:
                if y is not None:
                    #c = y.encode('cp1252')
                    b.append(y.encode('cp1252'))
                else:
                    b.append(None)
            tuple(b)
            itemsListNew.append(b)
        print(itemsListNew)
        return itemsListNew
    
    def startRoundsGUI(self, infoRoundList):
        # TenseList = ['Future Perfect', 'Past Perfect', 'Conditional', 'Future Perfect', 'Preterite', 'Future', 'Present Perfect', 'Conditional Perfect', 'Imperfect', 'Present', 'Past Perfect', 'Preterite (Archaic)']
        # ConfidenceList = ['High 3', 'Medium 2', 'Low 1', 'Wrong 0']
        # MoodList = ['Imperative Affirmative', 'Imperative Negative', 'Indicative', 'Subjunctive']
        # QuestionList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        # InfinitiveList = db.FindVerbList()
        #for x in range(0, 1000):
        #    locationList.append(fake.city())

        layout = [[sg.Text('Infinitive ' + infoRoundList[0]),
                   sg.Combo(infoRoundList[0], size=(20,1), key='-INFINITIVE-L02-')],
                  [sg.Text('Mood_english ' + infoRoundList[1]),
                   sg.Combo(infoRoundList[1], size=(20,1), key='-MOOD_ENGLISH-L02-')],
                  [sg.Text('Tense' + infoRoundList[2]), sg.Combo(infoRoundList[2], size=(20,1), key='-TENSE_ENGLISH-L02-')],
                  [sg.Text('yo'),
                   sg.Input(size=(20,1), key='-FORM_1S-L02-')],
                   [sg.Text('tú'),
                   sg.Input(size=(20,1), key='-FORM_2S-L02-')],
                   [sg.Text('él/ella/usted'),
                   sg.Input(size=(20,1), key='-FORM_3S-L02-')],
                   [sg.Text('nosotros(as)'),
                   sg.Input(size=(20,1), key='-FORM_1P-L02-')],
                   [sg.Text('vosotros(as)'),
                   sg.Input(size=(20,1), key='-FORM_2P-L02-')],
                   [sg.Text('ellos/ellas/ustedes'),
                   sg.Input(size=(20,1), key='-FORM_3P-L02-')],
                   [sg.Text('Gerund'),
                   sg.Input(size=(20,1), key='-GERUND-L02-')],
                   [sg.Text('Pastparticiple'),
                   sg.Input(size=(20,1), key='-PASTPARTICIPLE-L02-')],
                   [sg.Text('Confidence Level'), sg.Combo(self.ConfidenceList, key='-CONFIDENCE-L02-')],
                  [sg.Button('NEXT', bind_return_key=True), sg.Button('CANCEL')]
                  ]

        return layout
    
    def RoundsTabGUI(self, score):
        
        libTableSize = (1220, 10)

        libTableRounds = sg.Tab(
            'Round Info',

            [[sg.Text("Round Info")],
             [sg.Table(values=self.db.getListTmp(), headings=['infinitive', 'mood_english', 'tense_english'], key='-TABLE-L02-', enable_events=True, font=("Arial", 8), size=libTableSize, justification="left"), sg.Image(filename='AltInfo.PNG', size=(200,200)), sg.Image(filename='AltInfo2.PNG', size=(200,200))],
             [sg.Text('Score = ' + str(score)), sg.Input(size=(10, 1), key='-SCORE-L02-')],
             [sg.Text('infinitive'), sg.Combo(self.InfinitiveList, size=(15,1), key='-INFINITIVELIST-L02-')],
             [sg.Text('mood_english'), sg.Combo(self.MoodList, size=(15,1), key='-MOODLIST-L02-')],
             [sg.Text('tense_english'), sg.Combo(self.TenseList, size=(15,1), key='-TENSELIST-L02-')],
             [sg.Text('qestion number'), sg.Combo(self.QuestionList, size=(15,1), key='-QUESTIONLIST-L02-')],
             [sg.Button('Update Question', key='-UPDATE-QUESTION-BUTTON-L02-'),sg.Button('Update Random Question', key='-UPDATE-RANDOM-QUESTION-BUTTON-L02-')],
            [sg.Button('START', key='-START-BUTTON-L02-'),
             sg.Button('REFRESH', key='-REFRESH-BUTTON-L02-'),
             sg.Button('SEARCH', key='-SEARCH-BUTTON-L02-'),
             sg.Input(size=(20,1), key='-SEARCH-INUPUT-L02-'),
             sg.Button('UPDATE SEARCH', key='-UPDATE-SEARCH-BUTTON-L02-'),
             sg.Text('question Number'), sg.Combo(self.QuestionList, size=(3,1), key='-QUESTIONLIST2-L02-')],
             [sg.Table(values=self.db.getALLVerbs(), headings=['infinitive','mood_english','tense_english','yo' ,'tú' ,'él/ella/usted' ,'nosotros(as)' ,'vosotros(as)' ,'ellos/ellas/ustedes' ,'gerund','pastparticiple'], key='-TABLE2-L02-', enable_events=True, font=("Arial", 8), size=libTableSize, justification="left", max_col_width=16)],
             ],
            key='L02'
        )  # end of tab Record Label

        
        # libTableArtist = sg.Tab(
            # 'Artist',
            # [[sg.Text("Artists")],
                # [sg.Table(values=self.db.getAllArtists(), headings=[' Artist Name ', ' Age ', ' knownfor ',
                                                                    # '  Instrument  ', '      Band      '], key='-TABLE-L02-', enable_events=True, size=libTableSize, justification="left")],
                # [ sg.Button('UPDATE', key='-UPDATE-BUTTON-L02-'),
                # sg.Button('DELETE', key='-DELETE-BUTTON-L02-')]
             # ],
            # key='L02'
        # )

        # libTableAlbum = sg.Tab(
            # 'Album',
            # [[sg.Text("Albums")],
                # [sg.Table(values=self.db.getAllAlbums(), headings=['Title', 'Album Duration',
                                                                   # 'Cover Art URL', 'Averaqe Rating', 'Listeners', 'User Rating'], key='-TABLE-L03-', enable_events=True, size=libTableSize, justification="left")],
                
                # [sg.Button('UPDATE', key='-UPDATE-BUTTON-L03-'),
                # sg.Button('DELETE', key='-DELETE-BUTTON-L03-')]
              
            # ],
            # key='L03'
        # )

        # libTableSong = sg.Tab(
            # 'Song',
            # [[sg.Text("Songs")],

             # [sg.Table(values=self.db.getAllSongs(), headings=['Song', 'Album', 'Artist', 'Genre', 'Duration', 'Link',
                                                               # 'Release Year', 'Average Rating', 'Listeners', 'Rating'], key='-TABLE-L04-', enable_events=True, size=libTableSize, justification="left")],
             # [sg.Text("Rating"), sg.Slider(range=(0, 5),
                                           # default_value=0,
                                           # size=(25, 10),
                                           # orientation='horizontal',
                                           # font=('Helvetica', 12), key='-RATING-L04-'),
              # sg.Button('ADD RATING', key='-BUTTON-L04-'), 
                # sg.Button('UPDATE', key='-UPDATE-BUTTON-L04-'), 
                # sg.Button('DELETE', key='-DELETE-BUTTON-L04-')]
             # ],
            # key='L04'
        # )

        ### #### #### #### #### #### #### #### #### ###
        #                END OF LIB TABS              #
        ### #### #### #### #### #### #### #### #### ###

        RoundsTab = sg.Tab(
            'Play a Round',
            [[sg.TabGroup(
                [[
                    libTableRounds
                ]],
                key='tabgroupRounds',
                enable_events=True
            )  # end of TabGroup
            ]],

            key='Rounds_tab'

        )  # end of tab

        return RoundsTab
