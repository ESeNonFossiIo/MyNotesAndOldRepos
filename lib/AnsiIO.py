#!/usr/bin/env python
# This file is in the public domain

from sys import stdout as con

class AnsiIO(object):
    """Simple module to use ANSI control sequences for text mode graphics"""
    #
    def clear(self):
        """Clear screen"""
        con.write('\033[2J')
    #
    def pos(self,x,y):
        """Position cursor at x,y counting from the top left corner(0,0)"""
        con.write('\033[%d;%dH' % (x ,y) )
    #
    def put(self,x,y,c):
        """Write a character at a given x,y position counting from top left"""
        self.pos(x,y)
        con.write(c)
    #
    def putShift(self,shiftx,shifty,x,y,c):
        """Write a character at a given x,y position counting from (top+shiftx) (left+shifty)"""
        self.pos(x+shiftx,y+shifty)
        con.write(c)
    #
    def sync(self):
        """Synchronize all pending buffered characters to screen"""
        con.flush()
    #
    def init(self):
        """Initialize by clearing screen and disabling cursor"""
        self.clear()
        con.write('\033[?25l')
    #
    def reset(self):
        """Re-enable cursore and restore standard status."""
        con.write('\033[?25h\033[0m')
