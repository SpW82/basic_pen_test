#!/usr/bin/python

# Script that hold function to color input text using termcolor module
# Four colors available

from termcolor import colored

def color_red(text):
	return (colored(text, 'red'))

def color_green(text):
        return (colored(text, 'green'))

def color_yellow(text):
        return (colored(text, 'yellow'))

def color_blue(text):
        return (colored(text, 'blue'))


def main():
	t = input("Enter text to color red: ")
	print (color_red(t))

if __name__ == '__main__':
	main()
