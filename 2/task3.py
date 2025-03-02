import sys
import shutil
import os

def recursive_search(directory):
    for i in os.listdir(directory):
        if "." in i:
            # print(directory +  "/" + i)
            # print("./dst" + directory[5:] + "/" + i)
            if not os.path.exists("./dst" + directory[5:]):
                os.makedirs("./dst" + directory[5:])
            shutil.move(directory + "/" + i, "./dst" + directory[5:] + "/" + i)
        else:
            recursive_search(directory + "/" + i)

if len(sys.argv) != 2:
    exit("1 argument is required!")

if not os.path.exists(sys.argv[1] + "/src") or not os.path.exists(sys.argv[1] + "/dst"):
    exit("Both 'src' and 'dst' directories must be in given folder!")

recursive_search(sys.argv[1] + "/src")