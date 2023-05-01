stuffs = ['admin']
usernames = ['admin','accountant','manager','director','supervisor','finance','assistant']
for user in usernames:
    if user in stuffs:
        print('Hello ' + user + ',' + ' would you like to see a status report?')
    else:
        print('Thank you for logging in again ' + user)

     