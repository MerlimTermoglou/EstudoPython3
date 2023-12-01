import modulo

am = "I'm going back to 505 If it's a seven hour flight"
print (am)
enc = modulo.caesar(am,18)
print(modulo.caesar(enc, 18, decode = True))