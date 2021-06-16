import math
pi = math.pi

V = 1000
ra = float(input("Radius Anfang:"))
re = float(input("Radius Ende:"))
r = ra
loops = ((re - ra) *2)


print("Radius   Höhe       Oberfläche")
print("---------------------------------")

i = 0
while i <= loops:
    h = V / (pi * r * r)
    A = 2 * pi * r * (r + h)
    print("{0:.2f}    ".format(r), "{0:.2f}     ".format(h),"{0:.2f}      ".format(A))
    r= r+0.5
    i= i+1
