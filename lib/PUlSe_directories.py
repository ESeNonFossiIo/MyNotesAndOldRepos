"""
  This library is a collection of Classes and Functions to deal with folder and
  filenames.
"""

import os

def make_next_dir(  progress_dir="run", 
                    separation_char="_", 
                    base_directory="output/",
                    lenght=4):
  """ Make progressive directories.

    Look for a pattern among directories and make/return the next avaible 
    directory.

    Example:
      `run_000`
      `run_001`

      the output will be `run_002`

    Args:
        progress_dir (str): Name of the directory. 
        separation_char (str): Char that separe `progress_dir` and the number. 
        base_directory (str): Name of the directory that contains all 
          progressive directories.
        lenght (int): Number of digits. (In the example it is 3)

    Returns:
        string: Name of the next directory.
  """
  base_directory+="/"
  if not os.path.exists(base_directory):
    os.makedirs(base_directory)

  numbers=[]
  for name in os.listdir(base_directory):
    if (  os.path.isdir(os.path.join(base_directory, name)) and
          name.find(progress_dir)>=0 ) :
      numbers.append( int( str(name).replace(progress_dir + separation_char, '') ) )
  numbers.append(-1)
  maximum = str ( max(numbers) + 1 )
  zeroes =  "0" * ( lenght - len(maximum) )
  new_dir = os.path.normpath(base_directory + progress_dir + separation_char + zeroes + maximum)
  os.makedirs(new_dir)
  
  return new_dir

def get_next( filename = "name", 
              ext = "txt",
              directory = "./",
              separation_char = "_",
              lenght=4):
  """ Help to create progressive files.

    Look for a pattern among files and return the next avaible name.

    Example:
      `file_0000`
      `file_0002`

      the output will be `file_0003`

    Args:
        filename (str): Name of the file.
        ext (str): Extension of the file 
        separation_char (str): Char that separe `filename` and the number. 
        directory (str): Name of the directory that contains all 
          progressive files.
        lenght (int): Number of digits. (In the example it is 4)

    Returns:
        string: Name of the next file.
  """
  numbers=[]
  for name in os.listdir(directory):
    if ( name.find(filename)>=0 and  name.find(ext)>=0) :
      name = name.replace("."+str(ext),"")
      numbers.append( int( str(name).replace(filename + separation_char, '') ) )
  numbers.append(-1)
  maximum = str ( max(numbers) + 1 )
  zeroes =  "0" * ( lenght - len(maximum) )
  next_filename = filename + separation_char + zeroes + maximum
  return next_filename
  