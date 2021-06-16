dimension = int(input("Wie viele Dimensionen hat dein LGS:"))
i = 0
p = 0
k = []
while i < dimension:
    k.append([])
    while p <= dimension:
        if p < dimension:
            k[i].append(float(input(f"Spalte{i+1} x{p+1}:")))
        else:
            k[i].append(float(input(f"Spalte{i + 1} Ergebnis:")))
        p += 1
    i += 1
    p = 0


for zahl in k[0]:


print(k)










