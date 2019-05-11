szoveg = "map"
uj_szoveg = ""

for n in szoveg:
    if n == ' ':
        uj_szoveg += chr(32)
    elif n == "y":
        uj_szoveg += "a"
    elif n == "z":
        uj_szoveg += "b"
    else:
        converter = ord(n) + 2
        uj_szoveg += chr(converter)
        


print(uj_szoveg)


