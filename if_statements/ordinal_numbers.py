# This code uses if-elif-else chain in the for loop to print ordinal numbers
numbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th']
first = '1st'
second = '2nd'
third = '3rd'
for number in numbers:
    if first in number:
        print(first)
    elif second in number:
        print(second)
    elif third in number:
        print(third)
    else:
        print(number)