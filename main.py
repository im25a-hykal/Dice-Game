#Spielinstrucktionen


#alle Inputs und Variabeln(anzahl Punkte, Spieler...)
players = int(input("How many players do you have? "))
pointbarrier = int(input("What's the point barrier? "))
dicecount = int(input("How many dice do you have? "))


#Mainfunktion
#   jeder spieler durchläuft den folgenden loop
"""
    print: Spieler ... ist am zug
    print: drücken sie enter um zu würfeln oder space um aufzuhören.
    nach jedem wurf wird der aktuelle score revealed
    zusätzlich sieht man rechts die point barrier
    Fals Zeit besteht kann ein feature ein gebaut werden dass zeigt wo du in der rangliste
    wärst wenn du jetzt rausgehst
"""
#Auswertung und Rangliste(Scorebord)