from math import *
#Noch eine kleine Nachfrage eingebaut
check = "N"
while check == "N":
    länge = float(input("Länge des Quaders in m:"))
    breite = float(input("Breite des Quaders in m:"))
    höhe = float(input("Höhe des Quaders in m:"))

    print("Länge:  "+str(länge)+" m")
    print("Breite: "+str(breite)+" m")
    print("Höhe:   "+str(höhe)+" m")
    check = input("Wenn deine Eingaben richtig sind schreibe(J), ansonsten (N):")

print("Volumen: "+str(länge*breite*höhe)+" m^3")
print("Oberfläche: "+str(2*länge*breite+2*länge*höhe+2*breite*höhe)+" m^2")
print("Raumdiagonale: "+str(sqrt(länge * länge+breite*breite+höhe*höhe))+" m")