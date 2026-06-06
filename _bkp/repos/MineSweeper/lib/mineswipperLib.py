#!/usr/bin/env python

from lib.AnsiIO import AnsiIO as AnsiIO
import sys
import copy
import random
from funLib import *

class Game(object):
	"""This class contains all rules and development of the game."""
	#The following variable sets the distance of the board from the margin
	xMargin = 15
	yMargin = 15
	#Game variables
	win = True
	msg="You WIN!"
	field=''
	minesField=''
	#addimissible movements
	d=[	[-1,1],	[0,1],	[1,1],
		[-1,0],	 		[1,0],
		[-1,-1],[0,-1],	[1,-1]]

	def __init__(self):
		"""This function set the board and  positions of mines."""
		AnsiIO().clear()
		self.idim = int(raw_input("\t Insert the x dimension: "))
		self.jdim = int(raw_input("\t Insert the y dimension: "))
		self.numberOfMines = (self.idim*self.jdim)
		while (self.numberOfMines > (self.idim*self.jdim-1)):
			self.numberOfMines = int(raw_input("\t Insert the number of mines [the number of mines has to be less or equal than "+str(self.idim*self.jdim-1)+" ]: "))
		parameter = [self.idim, self.jdim, self.xMargin, self.yMargin, self.d]
		AnsiIO().clear()
		self.board = Board(parameter, self.numberOfMines)

	def status(self, what="mines"):
		"""This function clears the screen and if what = mines print the disposition of the mine while if what = status print the status of the game."""
		AnsiIO().clear()
		self.board.render(what)

	def check(self):
		"""This function checks if the game is over."""
		b=[self.idim, self.jdim]
		count=0
		if self.win:
			for i in xrange(self.idim):
				for j in xrange(self.jdim):
					# print self.board.field[i][j].status
					if self.board.field[i][j].status != 10:
					 	count+=1
			if count == (self.idim*self.jdim)-self.numberOfMines:
				return False
			else:
				return True
		else:
			return False

class Command(object):
	"""This class is needed to manage comands: it takes a comand in the form x##&& (where x=m,c,u , # is a number and & is a capital lettter) and do the action required."""
	xcoord=0
	ycoord=0
	command=''
	check=True

	def __init__(self, game, command):
		if command!='':
			self.game = game
			self.d = game.d
			self.word = command
			self.command = command[0]
			self.extractNum()
			self.extractWord()
			self.board = game.board
			self.bounds = [game.idim, game.jdim]
			C=field(self.xcoord,self.ycoord,self.bounds)
			if C.isAdimissible():
				self.action()
				self.check = True
			else:
				self.check = False
		else:
			self.check = False

	def extractNum(self):
		"""This method takes the comand and returns the number coordinate."""
		self.ycoord=0
		ten=1
		numWord=[]
		for i in xrange(len(self.word)):
			if(ord(self.word[i])<65):
				numWord.append(self.word[i])
		for i in xrange(len(numWord)-1,-1,-1):
			self.ycoord += ten*int(numWord[i])
			ten *= 10

	def extractWord(self):
		"""This method takes the comand and returns the letteral coordinate."""
		word = ''
		for i in xrange(len(self.word)):
			if(ord(self.word[i])>64 and ord(self.word[i])<96):
				word += self.word[i]
		self.xcoord = char2num(word) -1


	def action(self):
		"""This method takes the comand and the coordinates. It analises them and do the action."""
		x=self.xcoord
		y=self.ycoord
		b=self.bounds
		if self.command == 'm' and self.board.field[x][y].status == 10:
			self.board.field[x][y].status = 12
		elif self.command == 'c' and self.board.field[x][y].status == 12:
			self.board.field[x][y].status = 10
		elif self.command == 'e':
			self.game.msg="Close the game...."
			self.game.win=False
		elif self.command == 'u':
			C = field(x,y,b)
			self.propagate(C.coords())

	def propagate(self, p):
		"""This method is essential to unveil all free field."""
		x=p[0]
		y=p[1]
		b=self.bounds
		C = field(x,y,b)
		if self.board.field[x][y].status==10:
			if self.board.field[x][y].mines<9 and self.board.field[x][y].mines>0:
				self.board.field[x][y].status=self.board.field[x][y].mines
			elif self.board.field[x][y].mines==0:
				self.board.field[x][y].status=11
				for j in xrange(8):
					Cnew = C.move(self.d[j])
					if Cnew.isAdimissible():
						self.propagate(Cnew.coords())
			else:
				self.board.field[x][y].explode()
				self.game.msg="BOOOOOOOOOOOOOOOOOOOOOOOOOOMB!\n \t\t\t\t\tYou Lose! \n"
				self.game.win=False

class Board(object):
	"""This class generate a the Board Object that is the grid where playes puts their chips."""
	#
	def __init__(self, parameter, numMines):
		"""This method import all needed variables from the game class and then geneerates a game board."""
		self.numMines = numMines
		self.idim = parameter[0]
		self.jdim = parameter[1]
		self.bounds = [parameter[0], parameter[1]]
		self.xMargin = parameter[2]
		self.yMargin = parameter[3]
		self.d = parameter[4]
		self.io = AnsiIO()
		self.field = [[0]*self.jdim for i in xrange(self.idim)]
		for i in xrange(self.idim):
			for j in xrange(self.jdim):
				self.field[i][j]=field(i,j,self.bounds)
		self.MinesField()

	def MinesField(self):
		"""This function places mines on the board."""
		items = range(self.idim*self.jdim)
		random.shuffle(items)
		for i in xrange(self.numMines):
			c=field(items[i]%self.idim,items[i]/self.idim,self.bounds)
			self.field[c.x][c.y].setMines()
			for j in xrange(len(self.d)):
				cnew=c.move(self.d[j])
				if cnew.isAdimissible():
					if self.field[cnew.x][cnew.y].isThereMine():
						self.field[cnew.x][cnew.y].setNearMines()

	def render(self, what = "mines"):
		"""Given a status this function print the board."""
		self.io.clear()
		self.io.putShift(13,12, 0,0,'MineSwipper - Game')
		for j in xrange(self.jdim):
			self.io.putShift(self.xMargin,self.yMargin,j,-4,str(j))
			for i in xrange(self.idim):
				if what == "status":
					self.io.putShift(self.xMargin,self.yMargin,j,i,self.field[i][j].printStatus())
				else:
					self.io.putShift(self.xMargin,self.yMargin,j,i,self.field[i][j].printMine())
		for i in xrange(self.idim):
			char = num2char(i+1)
			char += ' '
			self.io.putShift(self.xMargin,self.yMargin,self.jdim+2, i,char[1])
			self.io.putShift(self.xMargin,self.yMargin,self.jdim+1, i,char[0])
		self.io.put(30,0,'')

class field(object):
	"""This class modelise a field"""
	def __init__(self, x, y, bounds):
		self.idim = bounds[0]
		self.jdim = bounds[1]
		self.bounds = bounds
		self.char = " 123456789# M@"
		self.x = x
		self.y = y
		self.status = 10
		self.mines = 0

	def setMines(self):
		self.mines = 9

	def setNearMines(self):
		self.mines += 1

	def setMark(self):
		if self.status == 10:
			self.status = 12

	def explode(self):
		if self.status == 10:
			self.status = 13

	def setUnmark(self):
		if self.status == 12:
			self.status = 10

	def isThereMine(self):
		if self.mines==9:
			return False
		else:
			return True

	def setUnveil(self):
		if self.status == 10:
			if self.mines!=9:
				self.status = self.mines
				return True
			else:
				return False

	def printMine(self):
		return self.char[self.mines]

	def printStatus(self):
		return self.char[self.status]

	def coords(self):
		return [self.x,self.y]

	def move(self, d):
		newx = self.x+d[0]
		newy = self.y+d[1]
		Cnew = field(newx,newy,self.bounds)
		return Cnew

	def isAdimissible(self):
		if self.y>=0 and self.y<self.jdim and self.x>=0  and self.x<self.idim:
			return True
		else:
			return False

class Player(object):
	"""This function is used as a variable to stored data on players. (Max 8 letters)"""
	name=""
	points=0

	def win(self):
		self.points+=1

	def __init__(self):
		AnsiIO().clear()
		self.name = raw_input('\t Insert the name of the player: ')
		self.points = 0
