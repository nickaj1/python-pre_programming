# This code modify the list and print a message to each person on the list.
invites = ['Christian','Nicholas','Kofi','Andy']
absent = [1]
absent = invites.pop(1)
print(absent + ' you were not able to make it i hope you show up next time.')
# inserting new person into the list with insert() method
invites.insert(1, 'Asoc')
print(invites)
# print message to each person on the list
invitation_messages1 = 'Hi ' + invites[0] + ' i invite you to my Dinner this weekend on Saturday, please do not miss out.'
invitation_messages2 = 'Hi ' + invites[1] + ' i invite you to my Dinner this weekend on Saturday, please do not miss out.'
invitation_messages3 = 'Hi ' + invites[2] + ' i invite you to my Dinner this weekend on Saturday, please do not miss out.'
invitation_messages4 = 'Hi ' + invites[3] + ' i invite you to my Dinner this weekend on Saturday, please do not miss out.'
print(invitation_messages1,invitation_messages2,invitation_messages3,invitation_messages4)

