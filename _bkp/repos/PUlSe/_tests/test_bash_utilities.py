import sys
sys.path.append("./lib/")
sys.path.append("./../lib/")
import os
import PUlSe_bash_utilities as pbash
import PUlSe_log as plog

def test_mkdir():
  """
    Test mkdir Function.
  """
  pbash.mkdir("_tmp")
  pbash.mkdir("_tmp/test1")
  pbash.mkdir("_tmp/test2")
  assert True

  log = plog.Log()

  pbash.mkdir("_tmp/test3", log=log)
  
  try:
    pbash.mkdir("_tmp/test3", error = True)
  except OSError:
    assert True  

  
def test_rm():
  """
    Test rm Function.
  """
  pbash.touch("_tmp.txt")
  pbash.rm("_tmp.txt")
  assert True
  
  log = plog.Log()
  pbash.touch("_tmp.txt")
  pbash.rm("_tmp.txt", log=log)
  pbash.rm("_tmp.txt")
  try:
    pbash.rm("_tmp.txt", error = True)
  except OSError:
    assert True
    
  
def test_rmdir():
  """
    Test rmdir Function.
  """
  pbash.mkdir("_tmp")
  pbash.mkdir("_tmp/test1")
  pbash.mkdir("_tmp/test2")
  log = plog.Log()
  pbash.rmdir("_tmp/test2", log=log)
  pbash.rmdir("_tmp/test3")
  try:
    pbash.rmdir("_tmp/test3", error = True)
  except OSError:
    assert True
    
  pbash.rmdir("_tmp/", all_content = True)
  assert True

def test_this_dir():
  """
    Test this_dir Function.
  """
  assert os.path.join( 
    os.path.dirname(os.path.realpath("./")), pbash.this_dir(False)) \
    == pbash.this_dir(True)
