fav_languages = {
    'Isaac': 'python',
    'Sarah': 'java',
    'Nick': 'java|python',
    'Akua': 'c',
    'Kofi' :'c++',
    'Obed' : 'javascript',
    'Norris' : 'java',
    'Peter' : 'ruby'
}
people = ['Nick','Akua','John','Newt','Obed','Aqua','Mensah','Ike']

# Looping through the list
for name in fav_languages.keys():
    if name in people:
        print('Thanks for responding ' + name)
    else:
        print('Please take me to the poll ' + name)
print(fav_languages[name])