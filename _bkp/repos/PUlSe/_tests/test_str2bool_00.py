import sys
import ConfigParser

sys.path.append("./lib/")
sys.path.append("./../lib/")
from PUlSe_string import str2bool

def test_str2bool_00():
    assert str2bool("T")
    assert str2bool("True")
    assert str2bool("1")
    assert not str2bool("0")
    assert not str2bool("F")
    assert not str2bool("false")
