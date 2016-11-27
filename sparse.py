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
    major_version = header[1]
    minor_version = header[2]
    file_hdr_sz = header[3]
    chunk_hdr_sz = header[4]
    blk_sz = header[5]
    total_blks = header[6]
    total_chunks = header[7]
    image_checksum = header[8]

    if magic != 0xED26FF3A:
      print("%s: %s: Magic should be 0xED26FF3A but is 0x%08X"
            % (me, path, magic))
      continue

  sys.exit(0)

if __name__ == "__main__":
  main()
