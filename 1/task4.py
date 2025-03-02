import sys
import itertools

if len(sys.argv) != 2:
    exit("One argument is required!")
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    exit("File doesn't exist!")

N = int(input("Enter 'N': "))
words = []
for i in range(len(lines)):
    words.append(lines[i].split())

words_list = list(itertools.chain(*words))
for i in range(len(words_list) - N + 1):
    for j in range(i, i + N):
        print(words_list[j], end=" ")
    print()