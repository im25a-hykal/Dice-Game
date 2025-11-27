import tkinter as tk
import random

root = tk.Tk()
root.geometry('1500x600')
players = {}
point_barrier = 0
dice_count = 0
decision = None
counter = 0
roll = 0
rolls = []
index = 0
total = 0
players_final_score = {}

current_player_name = tk.StringVar(value="")
roll_value = tk.StringVar(value="")
score_widget_frame = None

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
    global root, score_widgets_frame, current_player_name_var, last_roll_value_var
    global point_barrier, dice_count
    global roll_button, pass_button

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    #die drei container
    main_frame.grid_columnconfigure(0, weight=3)
    main_frame.grid_columnconfigure(1, weight=4)
    main_frame.grid_columnconfigure(2, weight=3)
    main_frame.grid_rowconfigure(0, weight=1)

    #Spalte Links
    score_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)
    score_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # Titel
    tk.Label(score_frame, text="Punkte aktuell:", font=("Arial", 12, "underline")).pack(pady=5)

    score_widgets_frame = tk.Frame(score_frame)
    score_widgets_frame.pack(fill=tk.Y, padx=15)


    #mittlere Spalte
    centre_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)
    centre_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    #titel
    tk.Label(centre_frame, text="Aktueller Spieler:", font=("Arial", 12, "underline")).pack(pady=5)
    #Aktuellerspieler
    tk.Label(centre_frame, textvariable=current_player_name, font="Arial, 16").pack(pady=5)
    #punktezahl die er geworfen hat
    tk.Label(centre_frame, textvariable=roll_value, font="Arial, 16", fg="green").pack(pady=5)
    #action buttons
    action_frame = tk.Frame(centre_frame)
    action_frame.pack(pady=20)
    roll_button = tk.Button(action_frame, text="Roll", command=lambda: roll_function(), font=('Arial', 12))
    roll_button.pack(side=tk.LEFT, padx=10)
    pass_button = tk.Button(action_frame, text="Pass", command=lambda: pass_function(), font=('Arial', 12))
    pass_button.pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Newstart", command=lambda: show_start_interface(), font=('Arial', 12)).pack(side=tk.LEFT, padx=10)


    #Rechte Spalte
    right_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)
    right_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

    #titel
    tk.Label(right_frame, text="Infos", font=("Arial", 12, "underline")).pack(pady=5)

    tk.Label(right_frame, text=f"Punkteschranke: {point_barrier}", font="Arial, 16").pack(pady=5)
    tk.Label(right_frame, text=f"Anzahl Würfel: {dice_count}", font="Arial, 16").pack(pady=5)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def update_ui():
    pass

def alert(message, duration_ms=5000):


    alert_window = tk.Toplevel(root)
    alert_window.title("Alert")


    alert_window.attributes('-topmost', True)


    label = tk.Label(alert_window, text=message, )
    label.pack(padx=10, pady=10)

    alert_window.after(duration_ms, alert_window.destroy)


    alert_window.update_idletasks()
    alert_window.lift()

def roll_function():

    global point_barrier, dice_count, current_player_name, roll_value, rolls, index, total, players_final_score, counter
    rolls = []
    counter = 0
    if roll_button or pass_button:
        roll_button.config(state=tk.DISABLED)
        pass_button.config(state=tk.DISABLED)

    while counter < dice_count:
        roll = random.randint(1, 6)
        rolls.append(roll)
        counter += 1
    roll_value.set(str(sum(rolls)))
    zusammengezaehlt = sum(rolls)
    players[current_player_name.get()] += zusammengezaehlt

    if players[current_player_name.get()] > point_barrier:
        lost = True
        players_final_score[current_player_name.get()] = -1
        players.pop(current_player_name.get())
    else:
        lost = False

    if lost:
        alert(f"geworfen: {roll_value} ", 5000)
    else:
        alert(f"Deine aktuellen Punkte: {players[current_player_name]}", 5000)
    root.after(3000, next_player)

def pass_function():
    pass


def next_player():
    pass







if __name__ == "__main__":
    show_start_interface()  # Baut das erste Interface auf

    root.mainloop()

