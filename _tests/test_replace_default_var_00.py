import sys
import ConfigParser

sys.path.append("./lib/")
sys.path.append("./../lib/")
from PUlSe_string import replace_default_var

def test_replace_default_var_00():
    dictionary = dict()
    dictionary[" "] = ""
    dictionary["this"] = ""
    dictionary["is"] = ""
    dictionary["the"] = ""
    dictionary["original"] = ""
    dictionary["string"] = "new"
    text = "this is the original string"
    text = replace_default_var(text, dictionary)
    assert text == 'new'
