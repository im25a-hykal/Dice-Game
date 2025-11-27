import random
import tkinter as tk
from tkinter import ttk, messagebox


# --- 1. Define Page Classes at the Top Level ---
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="--- Spiel Einstellungen ---", font=('Arial', 18)).pack(pady=20)

        # Input for Point Barrier
        ttk.Label(self, text="Punkteschranke:").pack()
        self.point_entry = ttk.Entry(self)
        self.point_entry.pack()
        self.point_entry.insert(0, "50")

        # Input for Dice Count
        ttk.Label(self, text="Anzahl Würfel:").pack()
        self.dice_entry = ttk.Entry(self)
        self.dice_entry.pack()
        self.dice_entry.insert(0, "3")

        # Input for Players
        ttk.Label(self, text="Spielernamen (Komma-getrennt):").pack()
        self.players_entry = ttk.Entry(self)
        self.players_entry.pack()
        self.players_entry.insert(0, "Alice, Bob, Charlie")

        # Button to start the game
        start_button = ttk.Button(self, text="Spiel starten",
                                  command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        """Reads inputs and initializes the game in the controller."""
        try:
            pointbarrier = int(self.point_entry.get())
            dicecount = int(self.dice_entry.get())
            names = [name.strip() for name in self.players_entry.get().split(',') if name.strip()]

            if not names:
                messagebox.showerror("Fehler", "Bitte Spielernamen eingeben.")
                return

            self.controller.initialize_game_data(pointbarrier, dicecount, names)
            self.controller.show_frame("GamePage")

        except ValueError:
            messagebox.showerror("Fehler", "Ungültige Zahleneingabe für Schranke/Würfel.")


class GamePage(ttk.Frame):
    """The game play interface."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Store the controller reference

        ttk.Label(self, text="Game", font=('Arial', 18)).pack(pady=20)

        def on_button_click():
            print("Button clicked! The command executed.")
            # You would put your application logic here
        def give_up():
            print("Button clicked! The command executed.")

        action_button_container = ttk.Frame(self)
        action_button_container.pack(pady=15)


        roll_button = tk.Button(
            self,
            text='Roll', command=lambda:on_button_click
        )
        roll_button.pack(pady=20)

        give_up_button = tk.Button(
            action_button_container,, text='give up' ,command =lambda:give_up()
        )
        give_up_button.pack(pady=20)
        button = ttk.Button(self, text="Back to Start", command=lambda: controller.show_frame("StartPage"))

        button.pack(side= 'right',pady=10)


class Game(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Dice Game Controller")
        self.geometry("600x450")  # Added geometry for clarity


        self.pointbarrier = 0
        self.dicecount = 0
        self.players = {}
        self.player_names_list = []
        self.current_player_index = 0
        self._game_ended = False

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # The call that was failing: It now works because show_frame is defined below.
        self.show_frame("StartPage")

    def initialize_game_data(self, barrier, count, names):
        """Sets game parameters from StartPage input."""
        self.pointbarrier = barrier
        self.dicecount = count
        self.player_names_list = names
        self.players = {name: 0 for name in names}
        self.current_player_index = 0

        if "GamePage" in self.frames and hasattr(self.frames["GamePage"], 'update_ui'):
            self.frames["GamePage"].update_ui()

    def show_frame(self, page_name):
        """Raises the selected frame to the top."""
        frame = self.frames[page_name]
        frame.tkraise()

        # Add logic to refresh the GamePage if it exists
        if page_name == "GamePage" and hasattr(frame, 'update_ui'):
            frame.update_ui()




if __name__ == "__main__":
    app = Game()
    app.mainloop()