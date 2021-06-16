import random
loop = True
while loop == True:
    def würfel(zahl):
        if zahl == 1:
            print("┌─────────┐")
            print("│         │")
            print("│    ●    │")
            print("│         │")
            print("└─────────┘")

        elif zahl == 2:
            print("┌─────────┐")
            print("│       ● │")
            print("│         │")
            print("│ ●       │")
            print("└─────────┘")

        elif zahl == 3:
            print("┌─────────┐")
            print("│    ●    │")
            print("│    ●    │")
            print("│    ●    │")
            print("└─────────┘")

        elif zahl == 4:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│         │")
            print("│ ●     ● │")
            print("└─────────┘")

        elif zahl == 5:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│    ●    │")
            print("│ ●     ● │")
            print("└─────────┘")

        elif zahl == 6:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│ ●     ● │")
            print("│ ●     ● │")
            print("└─────────┘")

    toh = int(input("Wer gewinnt? Hoch oder Tief? Für Hoch bitte eine 1, für Tief eine 0 eingeben:"))
    if toh == 1:
        print("Also Hoch gewinnt!")
    elif toh == 0:
        print("Also Tief gewinnt!")
    else:
        print("Ihre Zahl war ungültig")

    name = input("Geben Sie bitte noch Ihren Namen ein:")
    print(f"Sie würfeln zuerst, {name}.")

    a = random.randint(1, 6)
    b = random.randint(1, 6)

    print("Ihr Wurf:")
    würfel(a)
    print("Mein Wurf:")
    würfel(b)

    if toh == 1 and a > b:
        print(f"Sie haben gewonnen, {name}.")
        loop = False
    elif toh == 1 and a < b:
        print(f"Sie haben verloren, {name}.")
        loop = False
    elif toh == 0 and a < b:
        print(f"Sie haben gewonnen, {name}.")
        loop = False
    elif toh == 0 and a > b:
        print(f"Sie haben verloren, {name}.")
        loop = False
    else:
        print(f"Das war ein Unentschieden, {name}.")
        loop = True



