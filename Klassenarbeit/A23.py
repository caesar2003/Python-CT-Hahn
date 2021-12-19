n = int(input("Geben Sie die Anzahl der Zahlen ein:"))
i=0
a1 = 0
a2 = 1
while i < n:
    if i <= 1:
        result = i
        print(result)
        i += 1
    else:
        result = a1 + a2
        print(result)
        a1 = a2
        a2 = result
        i += 1
