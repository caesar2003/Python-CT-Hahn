
#ein anderer Ansatz, nun muss der Code bei mehreren Würfeln nicht ergänzt werden.
def wuerfel (zahl, zeile):
    if zahl == 6:
        if zeile == 1:
            return"┌─────────┐"
        elif zeile == 2:
            return"│ ●     ● │"
        elif zeile == 3:
            return"│ ●     ● │"
        elif zeile == 4:
            return"│ ●     ● │"
        elif zeile == 5:
            return "└─────────┘"
    elif zahl == 5:
        if zeile == 1:
            return"┌─────────┐"
        elif zeile == 2:
            return"│ ●     ● │"
        elif zeile == 3:
            return"│    ●    │"
        elif zeile == 4:
            return"│ ●     ● │"
        elif zeile == 5:
            return "└─────────┘"
    elif zahl == 4:
        if zeile == 1:
            return"┌─────────┐"
        elif zeile == 2:
            return"│ ●     ● │"
        elif zeile == 3:
            return"│         │"
        elif zeile == 4:
            return"│ ●     ● │"
        elif zeile == 5:
            return "└─────────┘"
    elif zahl == 3:
        if zeile == 1:
            return "┌─────────┐"
        elif zeile == 2:
            return"│       ● │"
        elif zeile == 3:
            return"│    ●    │"
        elif zeile == 4:
            return"│ ●       │"
        elif zeile == 5:
            return "└─────────┘"
    elif zahl == 2:
        if zeile == 1:
            return"┌─────────┐"
        elif zeile == 2:
            return"│       ● │"
        elif zeile == 3:
            return"│         │"
        elif zeile == 4:
            return"│ ●       │"
        elif zeile == 5:
            return "└─────────┘"
    elif zahl == 1:
        if zeile == 1:
            return"┌─────────┐"
        elif zeile == 2:
            return"│         │"
        elif zeile == 3:
            return"│    ●    │"
        elif zeile == 4:
            return"│         │"
        elif zeile == 5:
            return "└─────────┘"
    else:
        return"Ihre Zahl ist ungültig."


anzahl_wuerfel = int(input("Anzahl Würfel:"))
zahl = []
p = 1
while p <= anzahl_wuerfel:
    zahl.append(int(input("Geben Sie die "+str(p)+". Zahl ein:")))
    p = p + 1


z = 1
while z <= 5:
    for index in zahl:
        print(wuerfel(index, z), end= "")
    print()
    z = z + 1
