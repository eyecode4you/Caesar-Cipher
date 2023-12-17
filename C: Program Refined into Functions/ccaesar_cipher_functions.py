'''
ccaesar_cipher_functions.py
eyecode4you 18/12/23
Expanding on the concepts in: https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/    - A brilliant course I recommend!
'''
import random

def generate_key(n):
	''' Generate mapping of shifted chars using key '''
	CHARSET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
	key = {} #Create dict CHAR:SHIFTED CHAR
	cnt = 0
	for c in CHARSET: #for each char in set, add new dict key with value of shifted char cnt + shift value n
		key[c] = CHARSET[(cnt + n) % len(CHARSET)] #e.g. first iteration = 3 % 26 = 3, will wrap around when index is higher than 26
		cnt += 1
	return key
	
def display_key(key):
	''' display key mapping '''
	print("[KEY:]")
	for k in key.keys():
		print(k, end=' ')
	print()
	for x in key.keys():
		print('!', end=' ')
	print()
	for v in key.values():
		print(v, end=' ')
	
def encrypt(key, message):
	''' Take in message, iterate through, and shift '''
	SALT = ("`¬!\"£$%^&*\(\)-_=+\\|[{]};:'@#~,<.>/?")
	cipher = ""
	for c in message:
		if c in key:
			cipher += key[c] #build new string with shift map
		else:
			cipher += random.choice(SALT) #salt chars not in CHARSET
	return cipher

def get_decryption_key(key):
	''' map shifted chars back to original using key '''
	dkey ={}
	for c in key:
		#essentially reverse inputted key, e.g. shift = 3 and first 
		#input dict key = {A:D}, c will = A so first dkey entry = value 
		#of A then A itself = {D:A, etc...}
		dkey[key[c]] = c
	return dkey
	
'''PROGRAM RUN'''
kval = int(input("ENTER SHIFT VALUE: "))
key = generate_key(kval)

display_key(key)

message = input("\n\nENTER MESSAGE: ").upper()
cipher = encrypt(key, message)
print("\n\nENCRYPTED: ", cipher)

dkey = get_decryption_key(key)
dmessage = encrypt(dkey, cipher)
print("DECRYPTED: ", dmessage)
