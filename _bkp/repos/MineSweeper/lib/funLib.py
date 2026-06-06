"""Collection of utilities"""

def num2char(num):
    """This function convert numbers between 1 and 702 in letters between A and ZZ."""
    a = num%26
    b = num/26
    if a == 0:
        a = 26
        b = (num - 26)/26
    ca = chr(int(a) + 96).upper()
    if b>0:
        cb = chr(int(b) + 96).upper()
    else:
        cb = ''
    return cb + ca

def char2num(char):
    """This function convert letters between A and ZZ in numbers between 1 and 702."""
    num = 0
    for i in xrange(len(char)):
        num += (26**(i))*(ord(char[-(i+1)].lower()) - 96)
    return num
