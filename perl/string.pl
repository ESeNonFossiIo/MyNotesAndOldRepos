#!/usr/bin/perl

print "content-type: text/html \n\n"; #HTTP HEADER
## DEFINE A STRING TO REPLACE
$mystring = "Hello, am I about to be manipulated?!";

## PRINT THE ORIGINAL STRING
print "Original String: $mystring<br />";
#
## STORE A SUB STRING OF $mystring, OFFSET OF 7 AND LENGTH 10
$suboffsetANDlength = substr($mystring, 7, 10);
print "Offset of 7 and length of 10: $suboffsetANDlength<br />";

## CHANGE $mystring, OFFSET OF 7 AND LENGTH 10 AND 
## REPLACE SUB STR WITH "I want"
$suboffsetANDlength = substr($mystring, 7, 10, "I want");
print "mystring is now: $mystring<br />";
