#!/usr/bin/env bash

IN="bla@some.com;john@home.com"

arr=$(echo $IN | tr ";" "\n")

for x in $arr
do
	echo "> [$x]"
done
