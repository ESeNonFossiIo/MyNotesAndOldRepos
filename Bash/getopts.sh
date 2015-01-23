#!/bin/bash

while getopts dm name
do
	case $name in
		d)dopt=1;;
		m)mopt=1;;
		*)echo "Invalid arg";;
	esac
done

DT=`date '+%d %b'`

if [[ ! -z $dopt ]]
	then
	echo "Date is: " ${DT/ */}
fi
if [[ ! -z $mopt ]]
	then
	echo "Month is: " ${DT/* /}
fi

shift $(($OPTIND -1))