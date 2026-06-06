import sys
sys.path.append("./lib/")
sys.path.append("./../lib/")
import PUlSe_color as pcolor

def test_color():
  """
    Test Color Class.
  """
  style = pcolor.FormattedText("bold", "black", "red")
  assert style.write("test") == '\x1b[1;30;41mtest\x1b[0m'
  assert style.get_format() == '1;30;41'

def test_ansi_escape_sequence():
  """
    Test ANSIEscapeSequence Class.
  """
  aes = pcolor.ANSIEscapeSequence()

  assert aes.cmd("test") == '\x1b[test'

  assert aes.cur_pos(3, 2) == '\x1b[3;2H'

  assert aes.up("test") == '\x1b[testA'

  assert aes.down("test") == '\x1b[testB'

  assert aes.forward("test") == '\x1b[testC'

  assert aes.backward("test") == '\x1b[testD'

  assert aes.save_cur() == '\x1b[s'

  assert aes.restore_cur() == '\x1b[u'

  assert aes.erase() == '\x1b[2J'

  assert aes.erase_line() == '\x1b[K'