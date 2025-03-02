import sys

participants = dict()

try:
    with open(sys.argv[1], 'r', encoding='UTF-8') as file:
        for line in file:
            s = " ".join(line.split())
            participants[s.split()[0]] = int(s.split()[1])
except FileNotFoundError:
    exit("Файла нет -> вы идиот!")

participants = dict(sorted(participants.items(), key=lambda item: item[0]))

print("Sorted by key:")
for key in participants:
    print(key, participants[key])
print()
participants = dict(sorted(participants.items(), key=lambda item: item[1]))

print("Sorted by value:")
for key in participants:
    print(key, participants[key])
print()
try:
    N = int(input("Enter amount of points: "))
except ValueError:
    exit("Integer is required!")
participants = dict((k, v) for k, v in participants.items() if v > N)
with open("res.txt", 'w', encoding='UTF-8') as res_file:
    for key in participants:
        res_file.write(key+"\n")