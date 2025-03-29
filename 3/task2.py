import csv

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

try:
    file = open("3/countries.csv")
except FileNotFoundError:
    exit("File not found.")
reader = csv.reader(file)
next(reader)
filtered_countries = [row[0] for row in reader if lower_bound < float(row[2]) < upper_bound]

with open('3/results1.csv', mode='w', newline='') as res1:
    writer = csv.writer(res1)
    for country in filtered_countries:
        writer.writerow([country])

file.seek(0)
reader.__init__()
next(reader)
sorted_data = sorted(reader, key=lambda row: float(row[3]))

with open("3/results2.csv", mode='w', newline='') as res2:
    writer = csv.writer(res2)
    writer.writerows(sorted_data)