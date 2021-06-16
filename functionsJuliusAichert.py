import math

#Funktionen zum ^2 und ^3 berechnen
def square(num):
    return num * num
def cube(num):
    return num * num * num

#Funktionen zum berechnen der Eigenschaften des Kreises oder der Kugel
def kreisflaeche(radius):
    return math.pi * square(radius)
def kreisumfang(radius):
    return 2*math.pi * radius
def kugelvolumen(radius):
    return (4/3)*math.pi * cube(radius)
def kugeloberflaeche(radius):
    return 4*math.pi * square(radius)

#Hier beginnt das Hauptprogramm
radius = float(input("Bitte geben Sie den Radius in Meter ein:"))

kreisflaeche = kreisflaeche(radius)
kreisumfang = kreisumfang(radius)
kugelvolumen = kugelvolumen(radius)
kugeloberflaeche = kugeloberflaeche(radius)

print("Die Fläche eines Kreises mit dem Radius "+str(radius)+"m beträgt "+str(round(kreisflaeche, 2))+"qm")
print("Der Umfang eines Kreises mit dem Radius "+str(radius)+"m beträgt "+str(round(kreisumfang, 2))+"m")
print("Das Volumen einer Kugel mit dem Radius "+str(radius)+"m beträgt "+str(round(kugelvolumen, 2))+"cbm")
print("Die Oberfläche eines Kugel mit dem Radius "+str(radius)+"m beträgt "+str(round(kugeloberflaeche, 2))+"qm")