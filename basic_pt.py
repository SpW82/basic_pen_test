#!/usr/bin/python

from sshb import *
from ftpb import *
from c_text import *
from f_text import *
from ps_s3 import *
from hashb import *
import os

def main_ui():

#	print (standard_green('Basic'), standard_blue('Brute'), standard_red('Force'), color_yellow('\n SSH, FTP, Hashes'))
	try:
		while(True):
			print (standard_green('Basic'), standard_blue('Pen'), standard_red('Test'), color_yellow('\n SSH, FTP, Hashes'))
			print (color_yellow('\n====== '), color_green('Brute_modules'), color_yellow(' ======\n'),
			color_blue('\n 1. SSH/FTP_portscan\n 2. SSH_bruteForce\n 3. FTP_bruteForce\n 4. Hash_bruteForce'),
			color_red('\n *. ctrl-c_to_exit\n'),
			color_yellow('\n====== '), color_green('Brute_modules'), color_yellow(' ======\n'))

			choice = input(color_blue('[*] Enter module number: '))
			print ('\n')
			if choice == '1':
				os.system('clear')
				ps_s3_run()
				os.system('clear')
			elif choice == '2':
				os.system('clear')
				sshb_run()
				os.system('clear')
			elif choice == '3':
				os.system('clear')
				ftpb_run()
				os.system('clear')
			elif choice == '4':
				os.system('clear')
				hashb_run()
				os.system('clear')
			else:
				print (color_red('[*] Invalid Input'))
				input(colored("\n[*] Press Enter to return to main menu", 'yellow'))
				os.system('clear')

	except KeyboardInterrupt:
		print (color_red('\n[*] quitting\n'))
		quit()


if __name__ == '__main__':
	main_ui()

