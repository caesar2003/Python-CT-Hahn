def wuerfel (zahl, zeile):
    if zahl == 6:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│ ●     ● │", end="")
        elif zeile == 3:
            print("│ ●     ● │", end="")
        elif zeile == 4:
            print("│ ●     ● │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    elif zahl == 5:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│ ●     ● │", end="")
        elif zeile == 3:
            print("│    ●    │", end="")
        elif zeile == 4:
            print("│ ●     ● │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    elif zahl == 4:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│ ●     ● │", end="")
        elif zeile == 3:
            print("│         │", end="")
        elif zeile == 4:
            print("│ ●     ● │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    elif zahl == 3:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│       ● │", end="")
        elif zeile == 3:
            print("│    ●    │", end="")
        elif zeile == 4:
            print("│ ●       │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    elif zahl == 2:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│       ● │", end="")
        elif zeile == 3:
            print("│         │", end="")
        elif zeile == 4:
            print("│ ●       │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    elif zahl == 1:
        if zeile == 1:
            print("┌─────────┐", end="")
        elif zeile == 2:
            print("│         │", end="")
        elif zeile == 3:
            print("│    ●    │", end="")
        elif zeile == 4:
            print("│         │", end="")
        elif zeile == 5:
            print("└─────────┘", end="")
    else:
        print("Ihre Zahl ist ungültig.")

#Ende der Funktion wuerfel
#Hauptprogramm

zahl1 = int(input("Geben Sie die 1. Zahl ein:"))
zahl2 = int(input("Geben Sie die 2. Zahl ein:"))
zahl3 = int(input("Geben Sie die 3. Zahl ein:"))

x = 1
while x <= 5:
    wuerfel(zahl1, x)
    wuerfel(zahl2, x)
    wuerfel(zahl3, x)
    print()
    x = x + 1

