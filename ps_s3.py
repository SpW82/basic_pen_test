#!/usr/bin/python

import socket
from termcolor import colored
from f_text import *
from c_text import *


def portscanner(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if sock.connect_ex((host,port)):
		print (color_red(f"[-] Port {port} closed"))
	else:
		print (color_green(f"[+] Port {port} open"))


def portscanner_multi(host):
	p_list = [21, 22]
#	p_list  = range(1, 501)
	one_open = False
	for port in p_list:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if sock.connect_ex((host,port)):
			if port == 21:
				print (color_red(f"[-] Port {port} FTP closed"))
			else:
				print (color_red(f"[-] Port {port} SSH closed"))
		else:
			if port == 21:
				print (color_green(f"[+] Port {port} FTP open"))
				one_open = True
			else:
				print (color_green(f"[+] Port {port} SSH open"))
				one_open = True

	if one_open == False:
		print (color_red('[*] SSH/FTP ports closed/filtered'))


def ps_s3_run():
	print (standard_green('Ssh_Ftp'), standard_blue('Port'), standard_red('Scan'))
	host = input(color_blue("[*] Enter target host IP: "))
	print (color_yellow('[*] Scanning ssh/ftp ports ...'))
	portscanner_multi(host)
	input(color_yellow("\n[*] Press Enter to return to main menu"))

if __name__ == '__main__':
	ps_s3_run()
