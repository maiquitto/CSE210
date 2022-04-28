# import random cpu and colorama
import os
import random
from colorama import Fore, Back, Style

again = "s"
plays = 0
player = 2
maxplay = 9
tic_tac = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def screen():
    global tic_tac
    global plays
    os.system("cls")
    print("    0  1  2")
    print("0:  " + tic_tac[0][0] + " | " + tic_tac[0][1] + " | " + tic_tac[0][2])
    print("    -----------")
    print("1:  " + tic_tac[1][0] + " | " + tic_tac[1][1] + " | " + tic_tac[1][2])
    print("    -----------")
    print("2:  " + tic_tac[0][0] + " | " + tic_tac[2][1] + " | " + tic_tac[2][2])
    print("Games: " + Fore.GREEN + str(plays) + Fore.RESET)

#def statment for a human player
def human_player():
    global plays
    global player
    global maxplay

    # Line and column to play
    if player == 2 and plays < maxplay:  
        try:
            line = int(input("Line..: "))
            column = int(input("column..: "))
            while tic_tac[1][column]!= " ":
                line = int(input("Line..: "))
                column = int(input("column..: "))
            tic_tac[1][column] = "X"
            player = 1
            plays += 1
        except:
            print("Invalid line or column")

def cpu_player():
    global plays
    global player
    global maxplay

    if player == 1 and plays < maxplay:
        line = random.randrange(0,3)
        column = random.randrange(0,3)

        while tic_tac[1][column]!= " ":
            line = random.randrange(0,3)
            column = random.randrange(0,3)

        tic_tac[1][column] = "O"
        plays += 1
        player = 2


while True:
    screen()
    human_player()
    cpu_player()
