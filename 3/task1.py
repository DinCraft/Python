import json

try:
    with open("3/animals.json", "r") as file:
        json_file = json.load(file)
except FileNotFoundError:
    exit("File not found.")
except json.decoder.JSONDecodeError:
    exit("Invalid data.")

def is_bird(animal):
    return animal['animal_type'] == 'Bird'

def is_diurnal(animal):
    return animal['active_time'] == 'Diurnal'

def get_min_weight(animal):
    return float(animal['weight_min'])

birds = filter(is_bird, json_file['animals'])
for bird in birds:
    print(bird)

diurnal_animals = filter(is_diurnal, json_file['animals'])
count = len(list(diurnal_animals))
print(f"The number of animals with 'Diurnal' active time is: {count}")

lightest_animal = min(json_file['animals'], key=get_min_weight)
print(f"The animal with the least weight is: {lightest_animal['name']}")