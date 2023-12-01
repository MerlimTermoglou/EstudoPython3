def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])
msg = "Olá"
print (msg)
enc = (caesar(msg, 18))
print (enc)
print (caesar(enc, 18, decode = True))