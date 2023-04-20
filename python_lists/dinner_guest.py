# This code print a message indicating the number of invites using the Lenth 'len()' function.
invites = ['Christian','Nicholas','Kofi','Andy']
absent = [1]
absent = invites.pop(1)
print(absent + ' you were not able to make it i hope you show up next time.')
invites.insert(1, 'Asoc')
print(invites) 
invites.insert(0, 'Beatrice')
print(invites)
invites.insert(3, 'Akua')
print(invites)
invites.append('Gify')
print(invites)
invitation_message = 'Hello ' + invites[0] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message)
invitation_message1 = 'Hello ' + invites[1] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message1)
invitation_message2 = 'Hello ' + invites[2] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message2)
invitation_message3 = 'Hello ' + invites[3] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message3)
invitation_message4 = 'Hello ' + invites[4] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message4)
invitation_message5 = 'Hello ' + invites[5] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message5)
invitation_message6 = 'Hello ' + invites[6] + ' I found a bigger Dinner table for my get togther dinner this weekend on Saturday.'
print(invitation_message6)

# Printed the len() function with a message
print('I totally invite ' + str(len(invites)) + ' of my friends to the Dinner this weekend.') 
