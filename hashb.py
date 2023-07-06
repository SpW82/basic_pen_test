#!/usr/bin/python

import hashlib
from c_text import *
from f_text import *

def md5_hash(hash_v):
	hashjob1 = hashlib.md5()
	hashjob1.update(hash_v.encode())
	return str(hashjob1.hexdigest())

def sha1_hash(hash_v):
	hashjob2 = hashlib.sha1()
	hashjob2.update(hash_v.encode())
	return str(hashjob2.hexdigest())

def sha224_hash(hash_v):
	hashjob3 = hashlib.sha224()
	hashjob3.update(hash_v.encode())
	return str(hashjob3.hexdigest())

def sha256_hash(hash_v):
	hashjob4 = hashlib.sha256()
	hashjob4.update(hash_v.encode())
	return str(hashjob4.hexdigest())

def sha512_hash(hash_v):
	hashjob5 = hashlib.sha512()
	hashjob5.update(hash_v.encode())
	return str(hashjob5.hexdigest())


def crack_h(format, hashv ,file):
	hashed = ''
	for passwd in file.readlines():
		passwd = passwd.strip('\n')
		if format == '1':
			hashed = md5_hash(passwd)
		elif format == '2':
			hashed = sha1_hash(passwd)
		elif format == '3':
			hashed = sha224_hash(passwd)
		elif format == '4':
			hashed = sha256_hash(passwd)
		elif format == '5':
			hashed = sha512_hash(passwd)
		else:
			print (color_yellow("[*] Invalid input"))

		if hashed == hashv:
			print (color_green(f"[*] Success! Match found\n[+] Password:"),color_yellow(f"{passwd}\n"))
			return True

	print (color_red("[-] Password match not found"))
#		print (color_green(f"[*] {passwd} in MD5 : {md5_hash(passwd)}"))
#		print (color_yellow(f"[*] {hashv} : {hashv}"))


def hashb_run():
	print (standard_green("Hash\nCracker"), color_yellow("\nformats: 1.md5, 2.sha1, 3.sha224, 4.sha256, 5.sha512\n"))
#	print (color_yellow(f"[*] Hashed string: {hashed}"))
	format = input(color_blue("[*] Enter hashing format (1-5): "))
	hashv = input(color_blue("[*] Enter hash value to crack: "))
	f_name = input(colored("[*] Enter local file name: ", 'blue'))
	file = open(f_name, 'r')
	crack_h(format, hashv, file)
	input(color_yellow("[*] Press Enter to return to main menu"))


if __name__ == '__main__':
	hashb_run()
