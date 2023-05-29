# Defining a function that accept user input in a while loop

def make_album(artist, title):
    '''Return user input, neatly formatted'''
    person = {'artist_name':artist, 'album_title':title }
    return person

# Declaring a while loop that accept input and a break statement if user wish to quit process
while True:
        
        print('Search for your favorite artist') 
        print("Enter 'quit' to end program")

        name = input('Enter artist name')
        if name == 'quit':
             break
        
        title = input('Enter album title')
        if title == 'quit':
             break
        
        submit = input("Enter 'submit' when done or 'restart' to start program")
        if submit == 'submit':
                break
        elif submit == 'restart':
                continue

# Calling Dictionary with the user input as an argument
output = make_album(name,title)
print(output)        
                




# Defining another function with a while loop that accept user input and return an optional argument 'age'.

def your_self(first_name,last_name,age=0):
      '''Return user input information'''

      person = {'fname':first_name,'lname':last_name,}
      if age:
            person['age'] = age
      return person
     
# Declaring a while loop that accept input and a break statement if user wish to quit process
while True:
               
            fname = input('What is  your first name?')       
            if fname == 'stop':
                        break
            lname = input('What is your last name')
            if lname == 'stop':
                        break
            age = input('How old are you?')
            if age == 'stop':
                        break
            done = input("Enter 'Done' else Enter 'Stop' to quit program or 'restart' to continue")
            if done == 'Done':
                        break
            elif done == 'Stop':
                        continue
            
# Calling the function                   
output = your_self(fname,lname,age)
print(output) 




# Defining another function with a while loop that accept user input and return an optional argument 'track_no'.

def playlist(artist_name,album_title,track_no=0):
        '''Return user playlist'''
        if track_no:
         search = {'artist':artist_name,'album':album_title,'track':track_no}
        else:
                search = {'artist':artist_name,'album':album_title}
        return search

# Declaring a while loop that accept input and a break statement if user wish to quit process
while True:
        prompt = "Enter 'quit' to quit program at each stage "
       
        artist = input('Enter artist name: ')
        if artist == 'quit':
               break
        album = input('Enter album title: ')
        if album == 'quit':
               break
        track_no = input('Enter track number: ')

        done = input("Enter 'done' to display program")
        if done == 'done':
               break
        else:
               continue
        
# Calling function
result = playlist(artist,album,track_no)
print(result)




               
     
        

     








          

                  