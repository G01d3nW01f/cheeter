#!/usr/bin/python3

import os
import sys

if os.getuid() != 0:
  print("[!]You must execute as root, say the magic word")
  sys.exit()


os.system("chmod +x cheeter.py")
os.system("cp cheeter.py /usr/local/bin/cheeter")

print("Done.........")
