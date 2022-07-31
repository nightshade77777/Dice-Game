# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:11:17 2022

@author: SUHAANI
"""

'''

The players roll two 6-sided dice each and get points depending on what they
roll. There are 5 rounds in a game. In each round, each player rolls the two dice.
The rules are:
• The points rolled on each player’s dice are added to their score.
• If the total is an even number, an additional 10 points are added to their score.
• If the total is an odd number, 5 points are subtracted from their score.
• If they roll a double, they get to roll one extra die and get the number of points rolled added to
their score.
• The score of a player cannot go below 0 at any point.
• The person with the highest score at the end of the 5 rounds wins.
• If both players have the same score at the end of the 5 rounds, they each roll 1 die and
whoever gets the highest score wins (this repeats until someone wins).

Allows two players to enter their details, which are then authenticated to ensure that they are
authorised players.
2. Allows each player to roll two 6-sided dice.
3. Calculates and outputs the points for each round and
each player’s total score.
4. Allows the players to play 5 rounds.
5. If both players have the same score after 5 rounds, 
allows each player to roll 1 die each until someone wins.
6. Outputs who has won at the end of the 5 rounds.
'''

import random 
#password = letsgo
player1_input = input("Player1, please enter your name: ") 
player2_input = input("Player2, please enter your name: ") 
flag = "false"

while flag == "false":
    password = input("Please enter the password: ")
    if password == "letsgo":
        print("Welcome to my game ", player1_input, " and ", player2_input, "!")
        flag == "true"
        break
    else:
        print("Wrong password. Try again. ")



#ROUND 1 PLAYER 1 
i = 0
print()
print("Player 1, it is your turn to roll two dice. ")
print()

while i < 3:
    start_p1 = input("Enter 'roll' to play: ")
    start_p1.lower()
    
    if start_p1 == "roll":
        throw1 = random.randint(1, 6)
        i = i + 1
        throw2 = random.randint(1, 6)
        i = i + 1
        total_r1_p1 = throw1 + throw2
        
    if start_p1 != "roll":
        print("Try again. ")
        
print()     


print("Your total is ", total_r1_p1)
print()

#ROUND 1 PLAYER 2
k = 0
print("Player 2, it is your turn to roll two dice. ")
print()

while k < 3:
    start_p2 = input("Enter 'roll' to play: ")
    start_p2.lower()
    
    if start_p2 == "roll":
        throw1_r1_p2 = random.randint(1, 6)
        k = k + 1
        throw2_r1_p2 = random.randint(1, 6)
        k = k + 1
        total_r1_p2 = throw1_r1_p2 + throw2_r1_p2
        
    if start_p2 != "roll":
        print("Try again. ")
        
print()     
print("Your total is ", total_r1_p2)

#ROUND 2 PLAYER 1 

c = 0
print("Player 1, it is your turn to roll two dice. ")
print()

while c < 3:
    start_p1_r2 = input("Enter 'roll' to play: ")
    start_p1_r2.lower()
    
    if start_p1_r2 == "roll":
        throw1_r2_p1 = random.randint(1, 6)
        c = c + 1
        throw2_r2_p1 = random.randint(1, 6)
        c = c + 1
        total_p1_r2 = throw1_r2_p1 + throw2_r2_p1
        
    if start_p1 != "roll":
        print("Try again. ")

print()     
print("Your total is ", total_p1_r2)
print()

#ROUND 2 PLAYER 2

g = 0
print("Player 2, it is your turn to roll two dice. ")
print()

while g < 3:
    start_p2_r2 = input("Enter 'roll' to play: ")
    start_p2_r2.lower()
    
    if start_p2_r2 == "roll":
        throw1_r2_p2 = random.randint(1, 6)
        g = g + 1
        throw2_r2_p2 = random.randint(1, 6)
        g = g + 1
        total_p2_r2 = throw1_r2_p2 + throw2_r2_p2
        
    if start_p2_r2 != "roll":
        print("Try again. ")

print()     
print("Your total is ", total_p2_r2)
print()

new_total_p1 = total_r1_p1 + total_r1_p2
new_total_p2 = total_p2_r2 + total_p2_r2

if (new_total_p1 % 2) == 0:
    new_total_p1 = new_total_p1 + 10
else:
    new_total_p1 = new_total_p1 - 5
    
if (new_total_p2 % 2) == 0:
    new_total_p2 = new_total_p2 + 10
else:
    new_total_p2 = new_total_p2 - 5

if new_total_p1 > new_total_p2:
    print("Player 1, your total is ", new_total_p1)
    print("Congratulations!", player1_input,  "You won! ")
elif new_total_p1 < new_total_p2:
    print("Player 2, your total is: ", new_total_p2)
    print("Congratulations!", player2_input,  "You won! ")



    
    
    
    
    



