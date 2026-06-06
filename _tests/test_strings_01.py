import sys
import ConfigParser

sys.path.append("./lib/")
sys.path.append("./../lib/")
from PUlSe_string import retrieve_name

def test_string_00():
    x = 1
    assert retrieve_name(x) == 'x'
