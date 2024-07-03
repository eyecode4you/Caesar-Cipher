'''
caesar_cipher_functions.py
eyecode4you 17/12/23
Expanding on the concepts in: https://www.udemy.com/course/learn-modern-security-and-cryptography-by-coding-in-python/    - A brilliant course I recommend!
'''
import random, sys

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
	print("\n[KEY:]")
	for k in key.keys():
		print(k, end=' ')
	print()
	for x in key.keys():
		print('!', end=' ')
	print()
	for v in key.values():
		print(v, end=' ')
	print()
	
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
	
def get_schwifty():
	''' allow user to change shift value '''
	while 1:
		try:
			kval = int(input("ENTER SHIFT VALUE: "))
			key = generate_key(kval)
			break
		except:
			print("ERROR: ENTER AN INTEGER NUMBER!")
	return kval, key
	
'''PROGRAM RUN'''
kval, key = get_schwifty()
while 1:
	print("\n****CAESAR CIPHER****\n----------------------------")
	print("CURRENT SHIFT VALUE: ", kval)
	print("\nW: Change shift value\nS: View Key\nE: Encrypt a message\nD: Decrypt a message\nOther: Exit program")
	choice = input("\nSelect an option: ").upper()
	if choice == 'W':
		''' CHANGE SHIFT VALUE '''
		try:
			kval, key = get_schwifty()
		except:
			print("ERROR: PLEASE ENTER AN INTEGER NUMBER!")
	elif choice == 'S':
		display_key(key)
	elif choice == 'E':
		''' ENCRYPT A MESSAGE '''
		message = input("\n\n\t\tENTER MESSAGE: ").upper()
		cipher = encrypt(key, message)
		print("\t\tENCRYPTED: ", cipher)
	elif choice == 'D':
		''' DECRYPT A MESSAGE '''
		message = input("\n\n\t\tENTER MESSAGE: ").upper()
		dkey = get_decryption_key(key)
		dmessage = encrypt(dkey, message)
		print("\t\tDECRYPTED: ", dmessage)
	else:
		''' EXIT '''
		sys.exit(0)
