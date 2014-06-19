#!/bin/bash

#####################################
# script will walk through xml-dump from MCM
# DC-SOURCE will be the delimiter for creating
# individual bag-info.txt-files
# The split will be done with awk
#####################################


input=$1
itype=$2
deflang=DA
bagfile="/home/thw/tmp/mcm/bag-info.txt"
export MYLANG=$deflang


if [ $itype -gt 1 ]; then
  perl -pi -e 's/&lt;/</g' $input
  perl -pi -e 's/&gt;/>/g' $input
  perl -pi -e 's/&#xE6;/æ/g' $input
  perl -pi -e 's/&#xF8;/ø/g' $input
  perl -pi -e 's/&#xE5;/å/g' $input
  perl -pi -e 's/&#xD8;/Ø/g' $input
  perl -pi -e 's/&#xE9;/é/g' $input
fi



if [ $itype -gt 2 ]; then
  perl -pi -e 's/^\s{1,2}<Title>(.*)<\/Title>/DC-Title: \1/' $input
  perl -pi -e 's/<MCM.Data.DTO.ExtendedObjectInfo>/DC-SOURCE:/g' $input
  perl -pi -e 's/<Abstract>(.*)<\/Abstract>/DC-Abstract: \1/g' $input
  perl -pi -e 's/<Description>(.*)<\/Description>/DC-Description: \1/g' $input
  perl -pi -e 's/<ObjectID>(.*)<\/ObjectID>/DC-Identifier: \1/g' $input
  perl -pi -e 's/<Person Name=(.*) Role=(.*) \/>/DC-Creator: \2 \1/g' $input
  perl -pi -e 's/<Person Name=(.*) Role=(.*) \/>/DC-Creator: \2 \1/g' $input
  perl -pi -e 's/<Person Name=(.*) Role=(.*) \/>/DC-Creator: \2 \1/g' $input
  perl -pi -e 's/<Person Name=(.*) Role=(.*) \/>/DC-Creator: \2 \1/g' $input
  perl -pi -e 's/<Person Name=(.*) Role=(.*) \/>/DC-Creator: \2 \1/g' $input
  perl -pi -e 's/<DownloadURL>(.*)<\/DownloadURL>/DC-RELATION: \1/g' $input
  perl -pi -e 's/"//g' $input
fi
egrep "DC-" "$input" | sed 's/^[ ]*//g' > $bagf
