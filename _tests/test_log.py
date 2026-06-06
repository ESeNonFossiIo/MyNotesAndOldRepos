import sys
sys.path.append("./lib/")
sys.path.append("./../lib/")
import PUlSe_log as plog

def test_log():
  """
    Test Log Class
  """
  log = plog.Log(10, False, "test.txt")
  log.new_entry("test1","var1",True)
  log.new_entry("test2","var2",False)
  log.add_action("action","var")
  assert True

def test_action():
  """
    Test Action Class
  """
  log = plog.Action("test", "var")
  assert True
