k = float(input("Grundkapital in Euro:"))
z = float(input("Zinssatz in Prozent:"))/100
n = float(input("Laufzeit in Jahren:"))
i = 1

while i < n:
    k = k + k * z
    print("Das Kapital im "+str(i)+". Jahr beträgt: {0:.2f}".format(k))
    i = i + 1

k = k + k * z
print("Endkapital in Euro: {0:.2f}".format(k)+f" nach {int(n)} Jahren")