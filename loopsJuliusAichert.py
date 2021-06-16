i = 0
userLoop = float(input("Wie viele Loops möchtest du ausführen?:"))
a = 1
F = float(input("Aus welcher Zahl möchtest du die Wurzel ziehen?:"))
b = F
while i < userLoop:
    a = (a+b)/2
    b = F/a
    i+=1
    print("Werte nach dem "+str(i)+".Loop:")
    print("a="+str(a)+" b="+str(b))
print("Der Loop ist beendet")