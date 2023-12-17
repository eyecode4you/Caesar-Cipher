#caesar_cipher_encrypt.py
#eyecode4you 17/12/23
CHARSET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
CIPHER = 0
MESSAGE = ""

def main(args):
    return 0

if __name__ == '__main__':
	while not CIPHER in range(1,27):
		try:
			CIPHER = int(input("ENTER CIPHER VALUE (1-26): "))
		except:
			print()
	MESSAGE = input("ENTER MESSAGE TO ENCRYPT: ")
	
	print("\n****MAPPING****")
	print(CHARSET)
	for i in CHARSET:
		print(CHARSET[CHARSET.index(i) - CIPHER], end='')
	print("\n****MAPPING****\n\n")
	
	print("ENCRYPTED MESSAGE: ", end='')
	for i in MESSAGE.upper():
		if i not in CHARSET:
			print('-', end='')
			continue
		print(CHARSET[CHARSET.index(i) - CIPHER], end='')
