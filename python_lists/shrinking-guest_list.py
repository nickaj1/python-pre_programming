# This code remove guest from the list with pop() and del and print a message
invites = ['Christian','Nicholas','Kofi','Andy']
absent = [1]
absent = invites.pop(1)
print(absent + ' you were not able to make it i hope you show up next time.')
# added a list with insert() method
invites.insert(1, 'Asoc')
print(invites) 

invites.insert(0, 'Beatrice')
print(invites)

invites.insert(3, 'Akua')
print(invites)
# added a list with append() method
invites.append('Gify')
print(invites)
# assigned pop() method to remove guest from the list with an attach message
sorry_msg = invites.pop(0)
print('Hello ' + sorry_msg + ' i am sorry for any inconvenience, the table for the dinner can not contain enough.')

sorry_msg1 = invites.pop(1)
print('Hello ' + sorry_msg1 + ' i am sorry for any inconvenience, the table for the dinner can not contain enough.')

sorry_msg2 = invites.pop(2)
print('Hello ' + sorry_msg2 + ' i am sorry for any inconvenience, the table for the dinner can not contain enough.')

sorry_msg3 = invites.pop(3)
print('Hello ' + sorry_msg3 + ' i am sorry for any inconvenience, the table for the dinner can not contain enough.')

sorry_msg4 = invites.pop(0)
print('Hello ' + sorry_msg4 + ' i am sorry for any inconvenience, the table for the dinner can not contain enough.')
# print a message to remaining guest on the list
print('Hello ' + invites[0] + ' i will still be expexting to see you this weekends on my dinner')
print('Hello ' + invites[1] + ' i will still be expexting to see you this weekends on my dinner')
# assigning del to remove the remaining guest on the list
del invites[0]
print(invites)

del invites[0]
print(invites)
