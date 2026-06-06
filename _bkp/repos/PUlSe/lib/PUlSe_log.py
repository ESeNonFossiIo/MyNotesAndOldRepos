"""
  This is a Class to keep track of error and output of a project.
"""

class Action(object):
  """
    Struct used to modelize an action of the Log.
  """
  
  def __init__(self, action, text):
    """ Constructor.

      Constructor.

      Args:
          action (str): Name of the action.
          text (str): Text related to the action.
    """
    
    self.action = action
    self.text = text
  
class Log(object):
  """
    Helper to keep track of any change/variable/action of the program.
  """
  
  def __init__(self, lenght=100, verbose = False, filename = None):
    """ Constructor.

      Remove `directory`.

      Args:
          lenght (int): Lenght of the output.
          verbose (bool): If True, everything will be showed in the output.
          filename (file): If not `None`, everything will be saved on this 
            file.
    """
    self.lenght   = lenght
    self.log_values = dict()
    self.verbose = verbose
    self.filename = filename
    self.actions  = []
    
  def new_entry(self, name, value, output=False):
    """ Add a new entry to the Log.

      Add a new entry to the Log.

      Args:
          name (str): Name of the entry.
          value (str): Value of the entry.
          output (bool): If True, a message will be printed.
    """
    self.log_values[name] = value
    if output:
      print name + "  = " + value

  def add_action(self, action, text):
    """ Add an action to the Log.

      Add an action to the Log.

      Args:
          action (str): Name of the action.
          text (str): Text related to the action.
    """
    self.actions.append(Action(action,text))
