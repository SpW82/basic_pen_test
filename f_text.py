#!/usr/bin/python

# Script containing functions to design and color text 
# Uses module imports pyfiglet and termcolor
# Three options are available in four colors: 
# Banner3-d, standard and isometric2

from pyfiglet import Figlet
from termcolor import colored

# Banner3-d

#def three_d_green(text):
#	f = Figlet(font='banner3-D')
#	return (colored(f.renderText(text), 'green'))

#def three_d_red(text):
#        f = Figlet(font='banner3-D')
#        return (colored(f.renderText(text), 'red'))

#def three_d_yellow(text):
#        f = Figlet(font='banner3-D')
#        return (colored(f.renderText(text), 'yellow'))

#def three_d_blue(text):
#        f = Figlet(font='banner3-D')
#        return (colored(f.renderText(text), 'blue'))


# Standard


def standard_green(text):
        f = Figlet(font='standard')
        return (colored(f.renderText(text), 'green'))

def standard_red(text):
        f = Figlet(font='standard')
        return (colored(f.renderText(text), 'red'))

def standard_yellow(text):
        f = Figlet(font='standard')
        return (colored(f.renderText(text), 'yellow'))

def standard_blue(text):
        f = Figlet(font='standard')
        return (colored(f.renderText(text), 'blue'))


# Isometric2


#def isometric2_green(text):
#        f = Figlet(font='isometric2')
#        return (colored(f.renderText(text), 'green'))

#def isometric2__red(text):
#        f = Figlet(font='isometric2')
#        return (colored(f.renderText(text), 'red'))


#def isometric2_yellow(text):
#        f = Figlet(font='isometric2')
#        return (colored(f.renderText(text), 'yellow'))

#def isometric2_blue(text):
#        f = Figlet(font='isometric2')
#        return (colored(f.renderText(text), 'blue'))


# Testing
if __name__ == '__main__':
#	ht = three_d_green('Hi Jack !')
	ht_2 = standard_red('How are you?')
#	ht_3 = isometric2_blue('Are you good')
#	t_1 = three_d_yellow('Yellow and')
#	t_2 = three_d_blue('Blue testing')
#	print (ht,'\n',ht_2,'\n',ht_3)
#	print (t_1, t_2)
	print (ht_2)
