import pyautogui as pg
import time
import webbrowser

points = 0

#question
answer = pg.prompt(
"""
Which would you rather  do
a)Eat beets and watch battlestar galactica 
b)Eat as mamny M&M's as humanly possible 
c)Finish producing Threat Level Midnight 

"""
    )

# Give points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+= 3


#question
answer = pg.prompt(
"""
What is your greatest achievment?
a)Earning a black belt
b)Playing in a band
c)Founding the dundies  

"""
    )

# Give points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+= 3

#question
answer = pg.prompt(
"""
What is your ideal job
a)Sales Man of the Year 
b)Acounting, I think 
c)Boss, but friend first  

"""
    )

# Give points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+= 3

#question
answer = pg.prompt(
"""
Who is your rival 
a)Jimothy  
b)Math
c)Toby  

"""
    )

# Give points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+= 3



#END OF SURVEY

# Dwight
pg.alert ("You are...")
if points < 7:
    pg.alert("Dwight Kirt Schrute")
    webbrowser.open("https://www.youtube.com/watch?v=jgsPJVZY5pM")
# Kevin
if points >=7 and points < 10:
    pg.alert ("Kevin Mallone")
    webbrowser.open("https://www.youtube.com/watch?v=w4jI97DiHF8")
# Michael
if points >=10:
    pg.alert ("Michael Scott")
    webbrowser.open("https://www.youtube.com/watch?v=31g0YE61PLQ")


