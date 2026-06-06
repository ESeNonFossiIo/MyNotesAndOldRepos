"""
  This is a Class to deal with strings.
"""

from inspect import currentframe

def get_name_inside(  line,
                      begin_container="(",
                      end_container=")"):
  """ Get the value inside a container.

    Capture the text contained between two containers.

    Args:
      line (str): Text string
      begin_container (str): This delimiter is the one before the value to capture.
      end_container (str): This delimiter is the one after the value to capture.

    Returns:
      string: value contained between `begin_container` and `end_container`.
  """
  assert begin_container!="", " ERROR: `begin_container` is empty."
  assert end_container!="", " ERROR: `end_container` is empty."
  size = len(begin_container)
  start = line.find(begin_container)+size
  end = line.find(end_container, start)
  if end > -1 and start > -1:
    return line[start:end]
  else :
    return ""

def fill_dictionary_with_config_parser( dictionary,
                                        confparser,
                                        section):
  """ Use a ConfigParser to fill a dictionary.

    Capture the text contained between two containers.

    Args:
      dictionary (dict): Dictionary to fill.
      confparser (ConfigParser): ConfigParser Object where to take data for
        filling `dictionary`.
      section (str): Name of the section where to take data to fill the
        dictionary.
  """
  for entry in confparser.options(section):
    dictionary[entry] = confparser.get(section, entry)

def str2bool(string, YES=["yes", "true", "t", "1"]):
    """

    Convert a string to a bool.

    Args:
      string (string): Name to convert.
      YES (string): List of words accepted as true. They are no case sensitive.
    """
    return string.lower() in YES

def retrieve_name(var):
    """

    Return the name of a variable os string.

    Args:
      var (string): variable.
    """
    callers_local_vars = currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

def replace_default_var(string, dictionary):
    """

    Replace the content of string with the names of dictionary.

    Args:
      string (string): text.
      dictionary (dict): dictionary of terms to replace
    """
    for term in dictionary:
        string = string.replace(term, dictionary[term])
    return string
