"""
  This library is a collection of Classes and Functions to replace Bash
  commands in a python script.
"""

import os
import shutil

def rm(filename, error=False, log=None):
  """ Remove `file`.

    Remove `file`.

    Args:
        filename (str): Name of the file to remove.
        error (bool): If False any error will be suppressed.
        log (Log): Log Class where all info will be stored.

    Returns:
        error: In the case `error` is equal to True a possible error is 
          returned.
  """

  if log:
    log.add_action(action = "Remove file", text = filename)

  try:
    os.remove(filename)
  except OSError, e:
    if error:
      return e



def rmdir(directory, error=False, log=None, all_content=False):
  """ Remove `directory`.

    Remove `directory`.

    Args:
        directory (str): Name of the directory to remove.
        error (bool): If False any error will be suppressed.
        log (Log): Log Class where all info will be stored.
        all_content (boll): If True all subfolders/files included 
          will be deletted.

    Returns:
        error: In the case `error` is equal to True a possible error is 
          returned.
  """

  if log:
    log.add_action(action = "Remove directory", text = directory)

  try:
    if all_content:
      shutil.rmtree(directory, ignore_errors=True)
    else:
      os.removedirs(directory)
  except OSError, e:
    if error:
      return e

def mkdir(directory, error=False, log=None):
  """ Make `directory`.

    Make `directory`.

    Args:
        directory (str): Name of the directory to make.
        error (bool): If False any error will be suppressed.
        log (Log): Log Class where all info will be stored.

    Returns:
        error: In the case `error` is equal to True a possible error is 
          returned.
  """
    
  if log:
    log.add_action( action = "Make directory", text = directory)

  try:
    os.makedirs(directory)
  except OSError, e:
    if error:
      return e

def this_dir(abs_path = True):
  """ Return the name of the current directory.

    Return the name or the absolute path of the current directory.

    Args:
        abs_path (bool): If True this fuction will return the absolute path,
          otherwise only the name of the current directory.
        
    Returns:
        string: name/absolute path of the current directory.
  """
    
  current_dir = os.getcwd()
  if abs_path:
    return current_dir
  else:
    return current_dir.split(os.sep)[-1]

def touch( filename, times=None):
  """ Touch a file.

    Touch a file.

    Args:
        abs_path (bool): If True this fuction will return the absolute path,
        times(2-tuple of double): If times is None, then the file's access and 
          modified times are set to the current time. Otherwise, times must be 
          a 2-tuple of numbers, of the form (atime, mtime) which is used to set 
          the access and modified times, respectively.
  """
  
  fhandle = open(filename, 'a')
  try:
      os.utime(filename, times)
  finally:
      fhandle.close()
      