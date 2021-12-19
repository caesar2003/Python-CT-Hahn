import random

a1 = random.randint(1,6)
a2 = random.randint(1,6)
a3 = random.randint(1,6)
a = a1*100 + a2*10 +a3


b1 = random.randint(1,6)
b2 = random.randint(1,6)
b3 = random.randint(1,6)
b = b1*100 + b2*10 +b3

print("Spieler A:")
print(f"Wurf 1: {a1}")
print(f"Wurf 2: {a2}")
print(f"Wurf 3: {a3}")
print(f"gesamt: {a}")

print("\nSpieler B:")
print(f"Wurf 1: {b1}")
print(f"Wurf 2: {b2}")
print(f"Wurf 3: {b3}")
print(f"gesamt: {b}")
print("")


if a > b:
    print("Spieler A hat gewonnen!")
elif a == b:
    print("Unentschieden!")
else:
    print("Spieler B hat gewonnen!")