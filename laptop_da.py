### end result will ask "who are you working with?" "did you go out?" "anything unusual

## defining variables that will be used for each line
## pws = person we support

## determines who you were working with to set the variable

from ast import expr
import string
from tkinter.messagebox import YES


pws = input("Who are you working with? ")

first_line = "Staff prompted " + pws + " to wash their hands throughout the shift. "

second_line = "Staff reminded " + pws + " to use soap and water, while fully washing their hands. "

third_line = "Staff directed " + pws + " to socially distance themselves from others when possible. "

fourth_line = "Staff assisted " + pws + " with putting their mask on. If " + pws + "'s mask shifted, staff prompted them to adjust it."

## determines if you went out, which makes fourth_line necessary

outing = input("Did you go into the community? ")

if outing == ("Yes"):
    print(first_line + second_line + third_line + fourth_line)

elif outing == ("No"):
    print(first_line + second_line+ third_line)



#if outing ("yes")
#print(fourth_line)

## below is the inital code, inititally wanted to do outing -> yes -> 
## community integration -> then fourth_line... this seem excessive
## fourth_line == True (community_integration)

## print (first_line + second_line + third_line)




