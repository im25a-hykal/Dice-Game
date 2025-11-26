#Spielinstrucktionen
import random
import tkinter as tk
class Game(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in
    #game-interface und daten zuweisen
    def main_game(point_entry, dice_entry, players_entry):
        # Lese die Werte aus den Widgets aus
        try:
            global pointbarrier, dicecount, players  # <-- WARNUNG: Globale Variablen sind unsauber!
            pointbarrier = int(point_entry.get())
            dicecount = int(dice_entry.get())

            # Spielernamen verarbeiten (ersetzt playerselection)
            names = [name.strip() for name in players_entry.get().split(',') if name.strip()]
            players = {name: 0 for name in names}
            print("Spiel gestartet! Jetzt müsste das Spiel-Interface erscheinen.", players.keys(), flush=True)
            #hier werden alle startelemente gelöscht
            point_entry.pack_forget()
            dice_entry.pack_forget()
            players_entry.pack_forget()



        except ValueError:
            print("Ungültige Eingabe.")
    #start-interface
    def start_interface():
        """
        Diese funktion generiert das interface
        """
        root = tk.Tk()
        root.title("Dice Game")
        root.geometry("1200x400")

        tk.Label(root, text="Punkteschranke:").pack()
        point_entry = tk.Entry(root)
        point_entry.pack()

        tk.Label(root, text="Anzahl Würfel:").pack()
        dice_entry = tk.Entry(root)
        dice_entry.pack()

        tk.Label(root, text="Spielernamen (Komma-getrennt):").pack()
        players_entry = tk.Entry(root)
        players_entry.pack()

        # 2. Start-Button
        start_button = tk.Button(root, text="Spiel starten",
                                 command=lambda: main_game(point_entry, dice_entry, players_entry))
        start_button.pack()

        root.mainloop()
    start_interface()
    def show_frame():
        frame = self.

    counter = 0
    roll = 0
    #players = {}
    players_final_score = {}
    rolls = []






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
    #while len(players) >= 1:
        gameloop()