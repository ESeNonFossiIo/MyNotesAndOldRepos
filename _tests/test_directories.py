import sys
sys.path.append("./_lib/")
sys.path.append("./../_lib/")
import os
import PUlSe_directories as pdir
import PUlSe_bash_utilities as pbash

def test_make_next_dir():
  """
    Test make_next_dir Function.
  """
  base_dir = "_tmp/"

  print os.path.dirname(os.path.realpath(__file__))
  work_dir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(work_dir)
  
  pbash.mkdir(base_dir)
  pbash.rmdir(base_dir, all_content=True)
  
  assert not os.path.isdir("./"+base_dir)

  print os.listdir("./")
  
  next_dir = pdir.make_next_dir( progress_dir="run", 
                            separation_char="_", 
                            base_directory=base_dir,
                            lenght=4)
  assert os.path.exists("./"+os.path.join("_tmp/run_0000"))

  next_dir = pdir.make_next_dir( progress_dir="run", 
                            separation_char="_", 
                            base_directory=base_dir,
                            lenght=4)
  assert os.path.exists("./"+os.path.join("_tmp/run_0001"))

  for x in xrange(3):
    name = pdir.get_next( filename = "name", 
                      ext = "txt",
                      directory = "./_tmp",
                      separation_char = "_",
                      lenght=4)
    pbash.touch("./_tmp/"+name+".txt")

  assert os.path.exists("./"+os.path.join("_tmp/name_0002.txt"))

          
  try:
    os.removedirs(base_dir+"run_0000")
    os.removedirs(base_dir+"run_0001")
  except OSError:
    assert True

  pbash.rmdir(base_dir, all_content=True)
  assert True
