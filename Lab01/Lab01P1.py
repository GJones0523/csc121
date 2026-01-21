#
# Gregory Jones
# January 15, 2026
# This is a simple program to print someone's name from an input and the current
# date and time.
#

import datetime

name = input('What is your name? ')
print(f'Welcome to CSC121 {name}!')
print(f'Today is {datetime.date.today():%B %d, %Y}')
print('I hope you learn a lot of Python this semester!')
