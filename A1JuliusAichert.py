import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if a < b:
    print(f"Die Variable a hat den Wert {a}")
    print(f"Die Variable b hat den Wert {b}")
    print(f"Die Variable a ({a}) ist kleiner als b ({b})")
elif a > b:
    print(f"Die Variable a hat den Wert {a}")
    print(f"Die Variable b hat den Wert {b}")
    print(f"Die Variable a ({a}) ist größer als b ({b})")
else:
    print(f"Die Variable a hat den Wert {a}")
    print(f"Die Variable b hat den Wert {b}")
    print(f"Die Variable a ({a}) hat den gleichen Wert wie b ({b})")