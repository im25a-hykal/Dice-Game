import tkinter as tk
import random

root = tk.Tk()
root.geometry('500x300')
players = {}
point_barrier = 0
dice_count = 0


def show_start_interface():

    """
    Diese Funktion nimmt die gewünschten (players_input, pointbarrier, dice_input) in einem start interface auf.
    """

    clear_window()
    start_frame = tk.Frame(root)
    start_frame.pack(pady=20)

    #point_barrier
    point_barrier_label = tk.Label(start_frame, text="Was ist die point barrier?")
    point_barrier_label.pack()
    point_barrier_input = tk.Entry(start_frame)
    point_barrier_input.pack()

    #diceanzahl
    dice_input_label = tk.Label(start_frame, text="wie viele würfel")
    dice_input_label.pack()
    dice_input = tk.Entry(start_frame)
    dice_input.pack()

    #players
    players_label = tk.Label(start_frame, text="Geben sie alle Spieler ein(komma trennt die Spieler).")
    players_label.pack()
    players_input = tk.Entry(start_frame)
    players_input.pack()

    start_button = tk.Button(start_frame, text="Start", command=lambda: variable_assert(players_input, point_barrier_input, dice_input))
    start_button.pack()


def variable_assert(players_input, point_barrier_input, dice_input):
    global players, point_barrier, dice_count

    names = []

    point_barrier = int(point_barrier_input.get())
    dice_count = int(dice_input.get())

    players_raw = players_input.get().split(",")
    for name in players_raw:
        names.append(name)
    players = {name: 0 for name in names}

    clear_window()
    show_game_interface()

def show_game_interface():
    current_player_name_ = tk.StringVar(value="")
    last_roll_value_ = tk.StringVar(value="")

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    score_frame = tk.Frame(main_frame, bd=2, relief= tk.GROOVE)
    score_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
    tk.Label(score_frame, text="Aktuelle Punkte")

    global score_widgets_frame
    score_widgets_frame = tk.Frame(score_frame)
    score_widgets_frame.pack(fill=tk.Y)

    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20)

    active_frame = tk.Frame(main_frame)
    active_frame.pack(pady=10)

    tk.Label(active_frame, text="Punkte", font=("Arial", 12)).pack()
    #aktueler Name
    tk.Label(active_frame, textvariable=current_player_name_).pack()
    #Wurf


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()



if __name__ == "__main__":
    show_start_interface()  # Baut das erste Interface auf

    root.mainloop()
