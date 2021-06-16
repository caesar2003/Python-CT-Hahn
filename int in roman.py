import math
int = input("Gebe eine ganze Zahl zwischen 0 und 999 ein:")
tostr = str(int)
länge = len(tostr)

zuordnung = [
    {
    "0": "",
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
},
    {
    "0": "",
    "1": "X",
    "2": "XX",
    "3": "XXX",
    "4": "XL",
    "5": "L",
    "6": "LX",
    "7": "LXX",
    "8": "LXXX",
    "9": "XC",
},
    {
    "0": "",
    "1": "C",
    "2": "CC",
    "3": "CCC",
    "4": "CD",
    "5": "D",
    "6": "DC",
    "7": "DCC",
    "8": "DCCC",
    "9": "CD",
},
]

roman =""
index = []

for x in range(0, länge):
    index.insert(x, zuordnung[länge-1][tostr[x]])
    länge-=1
    roman += index[x]
print(roman)







