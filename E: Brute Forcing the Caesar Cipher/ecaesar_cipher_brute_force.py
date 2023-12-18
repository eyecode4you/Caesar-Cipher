'''
ecaesar_cipher_brute_force.py
eyecode4you 18/12/23
'''

def generate_key(n):
	''' Generate mapping of shifted chars using key '''
	CHARSET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
	key = {} #Create dict CHAR:SHIFTED CHAR
	cnt = 0
	for c in CHARSET:
		key[c] = CHARSET[(cnt + n) % len(CHARSET)]
		cnt += 1
	return key
	
def encrypt(key, message):
	''' Take in message, iterate through, and shift '''
	cipher = ""
	for c in message:
		if c in key:
			cipher += key[c] #build new string with shift map
		else:
			cipher += ' '
	return cipher
	
'''PROGRAM RUN'''
while 1:
	kval = 0
	key = generate_key(kval)
	message = input("\n\nENTER MESSAGE: ").upper()
	
	while kval < len(key):
		key = generate_key(kval)
		print("\n",encrypt(key, message), "KEY VALUE: ", kval)
		kval += 1
    
