#!/usr/bin/env python

import lib.mineswipperLib as mine
from lib.AnsiIO import AnsiIO as AnsiIO

yn = True
numberGame = 0
screen = AnsiIO()

player = mine.Player()

while yn:
	answer = "none"
	game = mine.Game()
	while game.check():
		game.status("status")
		screen.putShift(2,12, 0,0,' ')
		print "\nPLAYER:	", player.name
		print "SCORE: 	",player.points,"/",numberGame
		screen.putShift(2,22, 0,0,"Avaible comands:"	)
		screen.putShift(3,22, 0,0,"\t e: exit	 	 	")
		screen.putShift(4,22, 0,0,"\t m: mark field	 	")
		screen.putShift(5,22, 0,0,"\t c: unmark field	 ")
		screen.putShift(6,22, 0,0,"\t u: uncover field	 ")
		screen.putShift(7,22, 0,0,"\t e: exit	 ")
		screen.putShift(8,22, 0,0,"\t [x=m,c,u  -  #=number  -  &=ALPHA]")
		screen.putShift(10,12, 0,0,' ')
		command = raw_input("\n\tPlease, insert a comand in the form x##&&: ")
		newCommand = mine.Command(game,command)
	numberGame+=1
	if game.win:
		player.win()
	game.status()
	screen.putShift(8,22, 0,0,game.msg)
	while answer!='y' and answer!='n' :
		answer = raw_input("\n\tAnother game (y/n): ")
	if answer == 'n' or answer == 'N':
		yn = False
	# raw_input()
screen.clear()
