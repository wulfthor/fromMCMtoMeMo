#!/usr/bin/python

import re
import os, errno
import sys
import glob
import fnmatch
import shutil


# ../downloads/bagit/bagit-4.4/bin/bag create bobdylan_bag bag2

path='/tmp'
destbagit='/home/thw/bagit/newbags'
vidhome='/mnt/cifs/video/'
bagitcmd='/home/thw/downloads/bagit/bagit-4.4/bin/bag '

for dirpath, dirnames, files in os.walk(path):
  # now do each file
  for f in fnmatch.filter(files, 'bag-info.txt16*txt'):
    print f
    print "DO FILE"
    vidlist=[]
    dclist=[]
    for line in open(path + "/" + f):
      print "\tDO LINE .."
      if re.search('DC-RELATION',line):
        dclist.append(line)
        myLine=line.split('/')
        tmpFile=myLine.pop().rstrip()
        if re.search('mp4',tmpFile):
          print "\tOK for " + tmpFile + " for " + f + "\n"
          vidlist.append(tmpFile)
      if re.search('DC-Identifier',line):
        myLine=line.split(':')
        myID=myLine.pop().strip()
        print "\t" + myID
        bagpath=destbagit + "/data_" + myID
        try:
          print "TRY mkdir on " + bagpath
          os.makedirs(bagpath)
          dclist.append(line)
        except OSError as exc:
          if exc.errno == errno.EEXIST and os.path.isdir(path):
            print "ok err .. exist .."
            pass
          else: raise
      else:
        dclist.append(line)

    for vid in vidlist:
      srcvid=vidhome + vid
      print "TRY " + bagpath
      try:
        shutil.copy2(srcvid,bagpath)
      except  IOError as e:
        print e

    # create the bag
    tmpBagName="bag_" + myID
    tmpCmd=bagitcmd + "create " + tmpBagName + " " + bagpath
    print "\tDO BAG " + tmpCmd
    try:
      os.system(tmpCmd)
    except OSError as e:
      print e

    # add DC-metadata to the bag-info.txt file
    targetFile=destbagit + "/" + tmpBagName + "/" + "bag-info.txt"
    print "\tTRY: " + targetFile
    try:
      fh=open(targetFile, 'a')
      for dc in dclist:
        if not "DC-SOURCE" in dc:
          print "\tDCZZ: " + dc
          fh.write(dc)
      fh.close()
    except OSError as e:
      print e

    for dc in dclist:
      print "\tDC: " + dc

    print "DONE file\n\n"

