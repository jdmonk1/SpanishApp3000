import PySimpleGUI as sg
#from faker import Faker
#fake = Faker()
#Faker.seed(2)

### #### #### #### #### #### #### #### #### ###
#           START UPDATE TABLE TABS           #
### #### #### #### #### #### #### #### #### ###


class UpdateTab:
    def __init__(self, db):
        self.db = db

    def updateRecordLabelGUI(self):
        TenseList = ['Future Perfect', 'Past Perfect','Conditional','Future Perfect','Preterite','Future','Present Perfect','Conditional Perfect','Imperfect','Present','Past Perfect','Preterite (Archaic)']
        #for x in range(0, 1000):
        #    locationList.append(fake.city())

        layout = [[sg.Text('Infinitive'),
                   sg.Input(size=(10, 1), key='-INFINITIVE-U01-')],
                  [sg.Text('Mood_english'),
                   sg.Input(size=(10, 1), key='-MOOD_ENGLISH-U01-')],
                  [sg.Text("Tense"), sg.Combo(TenseList, key='-TENSE_ENGLISH-U01-')],
                  [sg.Text('yo'),
                   sg.Input(size=(10, 1), key='-FORM_1S-U01-')],
                   [sg.Text('tú'),
                   sg.Input(size=(10, 1), key='-FORM_2S-U01-')],
                   [sg.Text('él/ella/usted'),
                   sg.Input(size=(10, 1), key='-FORM_3S-U01-')],
                   [sg.Text('nosotros(as)'),
                   sg.Input(size=(10, 1), key='-FORM_1P-U01-')],
                   [sg.Text('vosotros(as)'),
                   sg.Input(size=(10, 1), key='-FORM_2P-U01-')],
                   [sg.Text('ellos/ellas/ustedes'),
                   sg.Input(size=(10, 1), key='-FORM_3P-U01-')],
                   [sg.Text('Gerund'),
                   sg.Input(size=(10, 1), key='-GERUND-U01-')],
                   [sg.Text('Pastparticiple'),
                   sg.Input(size=(10, 1), key='-PASTPARTICIPLE-U01-')],
                  [sg.Button('UPDATE', bind_return_key=True), sg.Button('CANCEL')]
                  ]

        return layout

    # def updateArtistGUI(self, instrumentList, albumNameList):
        # layout = [
            # [sg.Text("Update an Artist", size=(1270, 1))],

            # # Artist elements
            # [sg.Text("Artist Name"), sg.Input(key='-ARTIST-U02-')],

            # [sg.Text("Age"), sg.Slider(range=(1, 155),
                                       # default_value=42,
                                       # size=(40, 15),
                                       # orientation='horizontal',
                                       # font=('Helvetica', 12), key='-AGE-U02-')],
            # # Musician elements
            # [sg.Text("Instrument"), sg.Listbox(values=instrumentList, key='-INSTRUMENT-U02-', size=(10, 5))],
            # [sg.Text("Band Name"), sg.Input(key='-BAND-U02-')],

            # [sg.Text("Add album to artist?", size=(1270, 1))],

            # # Album elements
            # [sg.Text("Title"), sg.Listbox(values=albumNameList,
                                          # key='-TITLE-U02-', size=(50, 15))],
            # [sg.Button('UPDATE', bind_return_key=True), sg.Button('CANCEL')]

        # ]

        # return layout

    # def updateAlbumGUI(self):

        # layout = [[sg.Text('Title'),
                   # sg.Input(size=(10, 1), key='-TITLE-U03-')],
                  # [sg.Text("Duration"), sg.Slider(range=(30, 1000),
                                                  # default_value=42,
                                                  # size=(40, 15),
                                                  # orientation='horizontal',
                                                  # font=('Helvetica', 12), key='-DURATION-U03-')],
                  # [sg.Button('UPDATE', bind_return_key=True), sg.Button('CANCEL')]
                  # ]

        # return layout

    # def updateSongGUI(self, genreList):
        # yearList = list(range(2021, 999, -1))
        # layout = [[sg.Text('Title'),
                   # sg.Input(size=(10, 1), key='-TITLE-U04-')],
                  # [sg.Text("Genre"), sg.Listbox(values=genreList, key='-GENRE-U04-', size=(10, 5))],
                  # [sg.Text("Duration"), sg.Slider(range=(30, 1000),
                                                  # default_value=42,
                                                  # size=(40, 15),
                                                  # orientation='horizontal',
                                                  # font=('Helvetica', 12), key='-DURATION-U04-')],
                  # # Musician elements
                  # [sg.Text("Release Year"), sg.Combo(yearList, key='-YEAR-U04-')],
                  # [sg.Button('UPDATE', bind_return_key=True), sg.Button('CANCEL')]
                  # ]

        # return layout
