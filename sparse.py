#! /usr/bin/env python
#Script to find Image is sparse or ext4
# author : matrix

from __future__ import print_function
import getopt, posixpath, signal, struct, sys


def main():

    try:
    args = getopt.getopt(sys.argv[1:],
                               "v",
                               ["verbose"])
  for path in args:
    FH = open(path, 'rb')
    header_bin = FH.read(28)
    header = struct.unpack("<I4H4I", header_bin)

    magic = header[0]
    if magic == 0xED26FF3A:
      print("Sparse Image file)
      continue 
    if magic != 0xED26FF3A:
      print("ext4 Image file)     

  sys.exit(0)

if __name__ == "__main__":
  main()
