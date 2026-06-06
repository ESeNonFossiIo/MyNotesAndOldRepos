import sys
import ConfigParser

sys.path.append("./lib/")
sys.path.append("./../lib/")
import PUlSe_string as pstring


def test_get_name_inside():
  """
    Test get_name_inside Function.
  """
  # test1
  string = "val=[num]"
  assert pstring.get_name_inside(string, "[", "]") == "num"
  # test2
  string = "val=__VAL__[num]"
  assert pstring.get_name_inside(string, "__VAL__[", "]") == "num"
  # test3
  string = "val=__VAL__[num]"
  assert pstring.get_name_inside(string, "__VAL__[", "]") == "num"
  # test4
  string = "val=__VAL__"
  assert pstring.get_name_inside(string, "__VAL__[", "]") == ""

def test_fill_dictionary_with_config_parser():
  """
    Test fill_dictionary_with_config_parser Function.
  """
  config = ConfigParser.RawConfigParser()
  config.add_section('Section')
  config.set('Section', 'entry1', 'val1')
  config.set('Section', 'entry2', 'val2')
  config.set('Section', 'entry3', 'val3')
  dictionary = dict()
  pstring.fill_dictionary_with_config_parser( dictionary, config, "Section")
  assert dictionary['entry1'] == 'val1'
  assert dictionary['entry2'] == 'val2'
  assert dictionary['entry3'] == 'val3'
