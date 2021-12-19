import random
def wuerfel (zahl, zeile):
    if zeile == 1:
        print("┌─────────┐", end="")

    elif zahl == 6 and zeile == 2:
        print("│  ●   ●  │", end="")
    elif zahl == 6 and zeile == 3:
        print("│  ●   ●  │", end="")
    elif zahl == 6 and zeile == 4:
        print("│  ●   ●  │", end="")

    elif zahl == 5 and zeile == 2:
        print("│  ●   ●  │", end="")
    elif zahl == 5 and zeile == 3:
        print("│    ●    │", end="")
    elif zahl == 5 and zeile == 4:
        print("│  ●   ●  │", end="")

    elif zahl == 4 and zeile == 2:
        print("│  ●   ●  │", end="")
    elif zahl == 4 and zeile == 4:
        print("│  ●   ●  │", end="")

    elif zahl == 3 and zeile == 2:
        print("│  ●      │", end="")
    elif zahl == 3 and zeile == 3:
        print("│    ●    │", end="")
    elif zahl == 3 and zeile == 4:
        print("│      ●  │", end="")

    elif zahl == 2 and zeile == 2:
        print("│  ●      │", end="")
    elif zahl == 2 and zeile == 4:
        print("│      ●  │", end="")

    elif zahl == 1 and zeile == 3:
        print("│    ●    │", end="")

    elif zeile == 5:
        print("└─────────┘", end="")

    else:
        print("│         │", end="")
    #ende if
#Ende def wuerfel


a1 = random.randint(1,6)
a2 = random.randint(1,6)
a3 = random.randint(1,6)


b1 = random.randint(1,6)
b2 = random.randint(1,6)
b3 = random.randint(1,6)


i = 1
print("Spieler A:")
while i <= 5:
    wuerfel(a1, i)
    wuerfel(a2, i)
    wuerfel(a3, i)
    print("")
    i += 1

i = 1
print("\nSpieler B:")
while i <= 5:
    wuerfel(b1, i)
    wuerfel(b2, i)
    wuerfel(b3, i)
    print("")
    i += 1

print("")

a = a1*100 + a2*10 +a3
b = b1*100 + b2*10 +b3

if a > b:
    print("Spieler A hat gewonnen!")
elif a == b:
    print("Unentschieden!")
else:
    print("Spieler B hat gewonnen!")