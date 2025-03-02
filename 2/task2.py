import sys
import os

if len(sys.argv) != 2:
    exit("1 argument is required!")

print("Size: ", os.path.getsize(sys.argv[1]))