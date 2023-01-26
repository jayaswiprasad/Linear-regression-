
def a(text,s):
	r = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			r += chr((ord(char) + s-65) % 26 + 65)
		else:
			r += chr((ord(char) + s - 97) % 26 + 97)

	return r

text = "ATTACKATONCE"
s = 4
print ("plainText : " + text)
print ("key : " + str(s))
print ("Ciphertext: " + a(text,s))
