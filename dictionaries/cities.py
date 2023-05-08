# 
cities = {
   'Accra' : {
    'Fact': 'cultural attractions, shopping centers, and entertainment venues',
    'Population': 1.9,
    'Country': 'Ghana',
    },
    'London' : {
        'Fact': ' Big Ben, Buckingham Palace, British Museum, and Tower Bridge',
        'Population': 4.8,
         'Country': 'England',
        },

        'Paris': {
            'Fact' : ' Worldwide for the Louvre Museum, Notre-Dame cathedral, Eiffel tower and Lights',
            'Population': 2.1,
            'Country' : 'France',
        },
        'Milan': {
                'Fact':"Majestic Duomo Cathedral, the prominent opera La Scala, the medieval Sforza Castle, the dazzling Vittorio Emanuele II shopping arcade, and Leonardo Da Vinci's legacy",
                'Population': '',
                'Country': 'Italy',

        }
}


# Looping through Dictionary within the Dictionary
for name , details in cities.items():
        print('Name of City: ' + str(name))
        print('Information about city: ' + str(details))
