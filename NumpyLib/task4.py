import numpy as np
import csv
from collections import Counter

try:
	prices = []
	subscribers = []
	durations = []
	levels = []
	
	with open('NumpyLib/udemy_courses.csv', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			prices.append(float(row[1]))
			subscribers.append(int(row[2]))
			levels.append(str(row[4]))
			durations.append(float(row[5]))

		print(np.mean(prices))
		print(np.min(subscribers))
		print(np.max(durations))

		level_counts = Counter(levels)
		print(level_counts.most_common(1)[0][1])
except Exception as e:
	print(e)