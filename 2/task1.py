import sys
import os

if len(sys.argv) != 2:
    exit("1 argument is required!")

def recursive_search(directory, extension):
    for i in os.listdir(directory):
        if "." in i:
            if extension in i:
                print(i)
        else:
            recursive_search(directory + "/" + i, extension)

extension = input("Enter file extension: ")
recursive_search(sys.argv[1], extension)