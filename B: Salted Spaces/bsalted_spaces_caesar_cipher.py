#ainteractive_caesar_cipher_encrypt.py
#eyecode4you 17/12/23
CHARSET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")	
KEY = 0						#Character shift value
MESSAGE = ""					#Message to encrypt

import random
SALT = "`¬1!2\"3£4$5%6^7&8*9\(\)0-_=+\\|[{]};:'@#~,<.>/?" #I'll use this to add some randomness to space characters

def main(args):
    return 0

if __name__ == '__main__':
	while not KEY in range(1,27):		#Valid range is 1-26 (27 would cause index out of bound)
		try:
			KEY = int(input("ENTER KEY VALUE (1-26): "))
		except:
			print()
	MESSAGE = input("ENTER MESSAGE TO ENCRYPT: ")
	
	print("\n****MAPPING****")		#Show new character mapping
	print(CHARSET)
	for i in CHARSET:
		print(CHARSET[CHARSET.index(i) - KEY], end='')
	print("\n")
	
	print("ENCRYPTED MESSAGE (CIPHER): ", end='')
	for i in MESSAGE.upper():		#Replace spaces with random char
		if i not in CHARSET:
			print(random.choice(SALT), end='')
			continue
		print(CHARSET[CHARSET.index(i) - KEY], end='')
