import numpy as np
import csv
from collections import Counter

try:
	prices = []
	subscribers = []
	durations = []
	levels = []
	
	with open('6/udemy_courses.csv', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			prices.append(float(row[1]))
			subscribers.append(int(row[2]))
			levels.append(str(row[4]))
			durations.append(float(row[5]))

		print("avg:", np.mean(prices))
		print("min:", np.min(subscribers))
		print("max:", np.max(durations))

		level_counts = Counter(levels)
		print("level_counts:", level_counts.most_common(1)[0][1])
except Exception as e:
	print(e)