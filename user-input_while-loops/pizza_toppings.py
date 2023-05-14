# Looping through a user input and printing a message when a condition test is met
prompt = 'Enter toppings you want for your pizza'
prompt += "Enter 'quit' when done"

active = True
while active:
    name = input(prompt)
    print(name)
    if 'quit' in name:
        active = False
        print('Thanks for making us aware, we will add the toppings to your pizza')
