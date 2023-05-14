# Looping through a user input and printing a message if input is 'quit'
prompt = 'Enter toppings you want for your pizza'
prompt += "Enter 'quit' when done"

active = True
while active:
    name = input(prompt)

    if 'quit' in name:
        active = False
        break
    
    print('Thanks for making us aware, we will add the toppings to your pizza')
