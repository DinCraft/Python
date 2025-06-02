import pandas as pd

filename = "7/data_tallest_buildings.csv"

try:
    data = pd.read_csv(filename)
    print(data.sort_values(
		by='height_m', ascending=False)
		    .head(5)[['name', 'height_m']])
    print(data.sort_values(
		by='height_m', ascending=True)
		    .head(5)[['name', 'height_m']])
    heights = data['height_m']
    print(heights.min())
    print(heights.max())
    print(heights.mean())
    print(heights.median())

    print(data['country'].nunique())

    age = data['year_built']
    min_age = age.min()
    max_age = age.max()
    print(data[data['year_built'] == min_age][['name', 'year_built']])
    print(data[data['year_built'] == max_age][['name', 'year_built']])

    n = int(input("Enter floors amount: "))
    data['floors_amount'] = data['floors_above'] + data['floors_below_ground']
    filtered = data[data['floors_amount'] > n]
    print(filtered)

    year = int(input("Enter year: "))
    print(data[data['year_built'] == year][['name']])

    country = input("Enter country: ")
    print(data[data['country'] == country].shape[0])
except Exception as e:
	print(e)
