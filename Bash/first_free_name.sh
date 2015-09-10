#!/bin/bash

max=4
name="file"
ext="jpg"

num=$(ls -1 $name*.$ext | sort | tail -1 | sed "s#${name}_##" | sed "s#.${ext}##")
tmp=${num%%[!0]*}
num=${num#$tmp}
num=$(($num+1))
zeroes=$(($max - 1 - ${#num}))
zeroes=$( for (( c=1; c<=$zeroes; c++ )); do echo -n "0"; done )
touch ${name}_$zeroes$num.$ext
