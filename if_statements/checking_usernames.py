current_users = ['admin','accountant','manager','director','supervisor','finance','assistant']
new_users = ['finance','assistant','engineer','hr','deputy']
for user in new_users:
    if user in current_users:
        print('Sorry this rank '+ user.upper() + ' has been taken, change your rank. ')
    else:
        print('This rank, ' + user.upper() + ' is available.')