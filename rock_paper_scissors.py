#Author: Menesay
#01/08/2022
#Rock Scissors Paper game

import random
import time

print("-------------------------------------")
print("      Rock Scissors Paper Game       ")
print("             Menesay                 ")
print("-------------------------------------")

list = ['rock','scissors','paper' ]

computer = random.choice(list)
time.sleep(1)
user = input("rock (1), scissors (2), paper (3): ")

while user != '1' or user != '2' or user != '3':

    user = input("rock (1), scissors (2), paper (3): ")
    print("Please enter a valid string or integer")

    if user == '1' or user == '2' or user == '3':
        break
    

#resut=0 draws
#result=1 win
#result=2 lose

result = 1



if computer == 'rock':

    if user == 'rock' or user == '1':
        result = 0

    elif user == 'scissors' or user == '2':
        result = 2 

    elif user == 'paper' or user == '3':
        result = 1

elif computer == 'scissors':

    if user == 'rock' or user == '1':
        result = 1

    elif user == 'scissors' or user == '2':
        result = 0

    elif user == 'paper' or user == '3':
        result = 2

elif computer == 'paper':

    if user == 'rock' or user == '1':
        result = 2

    elif user == 'scissors' or user == '2':
        result = 1

    elif user == 'paper' or user == '3':
        result = 0

if user == '1':
    user = 'rock'

elif user == '2':
    user = 'scissors'

elif user == '3':
    user = 'paper'

time.sleep(0.5)
print("")
print("Computer is choicing...")
print("")
time.sleep(2)

print("-----------------------------")
print("Computers choice: "+computer)
print("Your choice: "+user)
print("-----------------------------")

print("")

time.sleep(0.5)

if result == 0:

    print("----------")
    print("   Draw!  ")
    print("----------")

elif result == 1:

    print("------------")
    print("  You win!  ")
    print("------------")

elif result == 2:

    print("------------")
    print("  You lose! ")
    print("------------")