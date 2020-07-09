from datetime import datetime
from random import randint
from time import sleep

odds = []
for i in range(60):
    if i % 2 == 1:
        odds.append(i)
for t in range(3):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute')
    #sleep(randint(1, 60))
