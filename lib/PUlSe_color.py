"""
  This library is a collection of Classes and Functions to deal with bash colors
  and formatted texts.
"""

class Style(object):
  """ Specify the style of the text.

    Specify the style of the text.

    Elements:
      all_attributes_off (enum): Remove all attributes.
      bold (enum): Bold text.
      italics (enum): Italics text.
      underscore (enum): Underscore text.
      blink (enum): Blick text.
      reverse (enum): Invert (Bg/Fg) the text.
      clean (enum): Clean the test.
  """
  all_attributes_off= 0
  bold = 1
  italics = 3
  underscore = 4
  blink = 5
  reverse = 7
  clean = 8
  
class BG(object):
  """ Specify the background color.

    Specify the background color.

    Elements:
      black (enum) = Black background.
      red (enum) = Red background.
      green (enum) = Green background.
      yellow (enum) = Yellow background.
      blue (enum) = Blue background.
      magenta (enum) = Magenta background.
      cyan (enum) = Cyan background.
      white (enum) = White background.
  """
  black = 40
  red = 41
  green = 42
  yellow = 43
  blue = 44
  magenta = 45
  cyan = 46
  white = 47

class FG(object):
  """ Specify the text color.

    Specify the text color.

    Elements:
      black (enum) = Black text.
      red (enum) = Red text.
      green (enum) = Green text.
      yellow (enum) = Yellow text.
      blue (enum) = Blue text.
      magenta (enum) = Magenta text.
      cyan (enum) = Cyan text.
      white (enum) = White text.
  """
  black = 30
  red = 31
  green = 32
  yellow = 33
  blue = 34
  magenta = 35
  cyan = 36
  white = 37

class FormattedText(object):
  """
    Create a style and format the text.
  """
  
  def __init__(self, style, fg, bg):
    """ Constructor.
    
      Args:
        style (Style): Define the style of the text.
        fg (FG): Define the color of the text.
        bg (BG): Define the background color of the text.
    """
    self.format = ';'.join([str(getattr(Style, style)), str(getattr(FG, fg)), str(getattr(BG, bg))])

  def begin(self):
    """ Start a formatted text.

      Start a formatted text.

      Returns:
        string: string to begin the formatted text.
    """
    return '\x1b[{0}m'.format(self.format)

  @staticmethod
  def end():
    """ Close a formatted text.

      Close a formatted text.

      Returns:
        string: string to close the formatted text.
    """
    return '\x1b[0m'

  def get_format(self):
    """ Get the format of the style.

      Get the format of the style.

      Returns:
        string: format of the style.
    """
    return self.format
  
  def write(self, text):
    """ Write the formatted text.

      Write the formatted text.

      Args:
        text (str): text of to print.
        
      Returns:
        string: format of the style.
    """
    return self.begin() + str(text) + self.end()

class ANSIEscapeSequence(object):
  """
    Wrapper for ANSI Escape Sequence codes.
  """
  def __init__(self):
    """ Constructor.
    """  
    self.ESC = '\x1b['

  def cmd(self, arg):
    """ Define a command.

      Define a command.

      Args:
        arg (str): argument of the command.
        
      Returns:
        string: string of the command related to `arg`.
    """
    return self.ESC+arg

  def cur_pos(self, row, col):
    """ Move cursor to a new position.

      Move cursor to (`row`,`pos`).

      Args:
        row (int): new row of the cursor position.
        col (int): new column of the cursor position.
        
      Returns:
        string: string of the command.
    """
    return self.cmd(str(row)+";"+str(col)+"H")

  def up(self, num):
    """ Move cursor up.

      Move cursor `num` rows up.

      Args:
        num (int): number of rows.
        
      Returns:
        string: string of the command.
    """
    return self.cmd(str(num)+"A")

  def down(self, num):
    """ Move cursor down.

      Move cursor `num` rows down.

      Args:
        num (int): number of rows.
        
      Returns:
        string: string of the command.
    """
    return self.cmd(str(num)+"B")

  def forward(self, num):
    """ Move cursor forward.

      Move cursor `num` columns forward.

      Args:
        num (int): number of columns.
        
      Returns:
        string: string of the command.
    """
    return self.cmd(str(num)+"C")

  def backward(self, num):
    """ Move cursor backward.

      Move cursor `num` columns backward.

      Args:
        num (int): number of columns.
        
      Returns:
        string: string of the command.
    """
    return self.cmd(str(num)+"D")

  def save_cur(self):
    """ Save cursor position.

      Save cursor position.
        
      Returns:
        string: string of the command.
    """
    return self.cmd("s")

  def restore_cur(self):
    """ Restore cursor position.

      Restore cursor position.
        
      Returns:
        string: string of the command.
    """
    return self.cmd("u")

  def erase(self):
    """ Erase.

      Erase.
        
      Returns:
        string: string of the command.
    """
    return self.cmd("2J")

  def erase_line(self):
    """ Clean current line.
    
      Clean current line.
        
      Returns:
        string: string of the command.
    """
    return self.cmd("K")

