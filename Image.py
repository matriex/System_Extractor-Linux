# -*- coding: utf-8 -*-


import sys, os

try:
    NEW_DATA_FILE = str(sys.argv[1])
except IndexError:
   print ("\nusage is: \n\n      py cha cha \n\n")
   try:
       input = raw_input
   except NameError: pass
   input ("Press ENTER to exit...\n")
   sys.exit()
def main(argv):

    new_data_file = open(NEW_DATA_FILE, 'rb')
fmh = new_data_file.read(28)
header = struct.unpack("<I4H4I", fmh)
magic=header(0)
if magic != 0xED26FF3A:
	print("\nExt4 Image file\n")
new_data_file.close()


if __name__ == "__main__":
    main(sys.argv)
