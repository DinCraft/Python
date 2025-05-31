import csv
from docxtpl import DocxTemplate
from collections import defaultdict

# Шаг 1: Чтение данных из файла
data = []
with open('data_marathon.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        data.append(row)

# Шаг 2: Обработка данных
# Группируем данные по году и городу
grouped_data = defaultdict(list)

for row in data:
    year = row['год']
    city = row['город']
    male_winner = row['имя победителя-мужчины']
    male_time = row['время на дистанции (часы:минуты:секунды)']
    female_winner = row['имя победителя-женщины']
    female_time = row['время на дистанции (часы:минуты:секунды)']
    
    grouped_data[year].append({
        'city': city,
        'male_winner': male_winner,
        'male_time': male_time,
        'female_winner': female_winner,
        'female_time': female_time
    })

# Шаг 3: Создание документа DOCX
for year, results in grouped_data.items():
    doc = DocxTemplate("template.docx")  # Замените на путь к вашему шаблону
    context = {
        'year': year,
        'results': results
    }
    doc.render(context)
    doc.save(f'results_{year}.docx')

print("Документы успешно созданы!")