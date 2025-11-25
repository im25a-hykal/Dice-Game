#Spielinstrucktionen
import random

#alle Inputs und Variabeln(anzahl Punkte, Spieler...)
pointbarrier = int(input("What's the point barrier? "))
dicecount = int(input("How many dice do you have? "))
counter = 0
roll = 0
players = {}
players_final_score = {}
rolls = []
def playerselection():
    while 'done' not in players and 'Done' not in players:
        player_name = input("What's the player name? ")
        players[player_name] = 0
    players.popitem()

playerselection()
print(list(players.keys()))
def gameloop():
    global counter
    global roll
    global rolls
    global players
    global players_final_score

    for player in players:
        if players[player] >= 0:
            decision = input(f'do you want to roll {player}? (y or n) ')
            if decision == 'y':
                while dicecount > counter:
                    roll = random.randint(1, 6)
                    rolls.append(roll)
                    counter += 1

                counter = 0
                total = sum(rolls)
                players[player] += total

                if players[player] >= pointbarrier:
                    lost = ' (you lost)'
                    players[player] = -1
                    players_final_score[player] = players[player]

                else:
                    lost = ''

                print(f'your total is {total} these are your rolls:{rolls}{lost}')
                rolls = []

            elif decision == 'n':
                players_final_score[player] = players[player]

    for player in players_final_score:
        if player in players:
            del players[player]
while len(players) >= 1:
    gameloop()

print(players)
sorted_players = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))
print(sorted_players.keys())
print (players_final_score)