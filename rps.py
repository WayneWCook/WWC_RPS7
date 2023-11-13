# Rockl Paper Scissors
# Wayne Cook
# 12 November 2023
# Purpose: Create a fun game of Rock Paper Scissor that remembers your past plays
# Force a new change in this file

import random
from datetime import*

class statistics:
    rps = ["Rock","Paper","Scissors"]
    games = 0
    wins = 0
    losses = 0
    ties = 0
    def print_statistics(self):
        print(f"In {statistics.games} games, you have {statistics.wins} wins, {statistics.losses} losses & {statistics.ties} ties.")

# The main logic for the game.
def play_rps():
    comp = random.choice(statistics.rps)
    use = int(input("Choose:\n1. Rock\n2. Paper\n3. Scissors\nChoice:"))
    user = statistics.rps[use - 1]
    statistics.games += 1
    print(f"The computer chose {comp} and you chose {user}")
    if (comp == user):
        statistics.ties += 1
    elif ((user ==  "Rock" and comp == "Scissors") or (user ==  "Paper" and comp == "Rock") or
          (user == "Scissors" and comp == "Paper")):
        statistics.wins += 1
    else:
        statistics.losses += 1

def main():
    print("Welcome to Rock, Paper, Scissors.")
    name = input("What is your name? ")
    filename = name + '.txt'
    print(filename)
    try:
        fhand = open(filename,'r')
        print(f"{filename} is open.")
        statistics.games += int(fhand.readline())
        #print(f"{statistics.games} games.")
        statistics.wins += int(fhand.readline())
        statistics.losses += int(fhand.readline())
        statistics.ties += int(fhand.readline())
        fhand.close()
        print("Welcome back!")
    except:
        print("Enjoy the game")
    statistics.print_statistics(None)
    loop = True
    while loop:
        play_rps()
        statistics.print_statistics(None)
        again = None
        while (again != 'y' and again != 'n'):    # Loop until either n or y is entered.
            again = input("Do you want to play again? (y|n): ").lower()
        if again == 'n':
            loop = False    # For user typing no (n), exit the loop. This is the end my friend.
    # Now write the file:
    fhand = open(filename, 'w')
    fhand.write(f"{statistics.games}\n")
    fhand.write(f"{statistics.wins}\n")
    fhand.write(f"{statistics.losses}\n")
    fhand.write(f"{statistics.ties}\n")
    fhand.close()

# Now start the whole program
main()
