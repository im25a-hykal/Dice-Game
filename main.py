#Spielinstrucktionen
import random

#alle Inputs und Variabeln(anzahl Punkte, Spieler...)
pointbarrier = int(input("What's the point barrier? "))
dicecount = int(input("How many dice do you have? "))
counter = 0
roll = 0
players = []
rolls = []
def playerselection():
    while 'done' not in players:
        player_name = input("What's the player name? ")
        players.append(player_name)
    players.pop()

playerselection()
print(players)

for player in players:
    decision = input(f'do you want to roll {player}? (y or n) ')
    if decision == 'y':
        while dicecount > counter:
            roll = random.randint(1, 6)
            rolls.append(roll)
            counter += 1
        counter = 0
        total = sum(rolls)
        print(f'your total is {total} these are your rolls:{rolls}')

"""
    print: Spieler ... ist am zug
    print: drücken sie enter um zu würfeln oder space um aufzuhören.
    nach jedem wurf wird der aktuelle score revealed
    zusätzlich sieht man rechts die point barrier
    Fals Zeit besteht kann ein feature ein gebaut werden dass zeigt wo du in der rangliste
    wärst wenn du jetzt rausgehst
"""
#Auswertung und Rangliste(Scorebord)