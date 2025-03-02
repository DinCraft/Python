import datetime

date2 = datetime.date.today()

day = input("Enter day (DD): ")
if len(day) != 2 or int(day) < 1 or int(day) > 31 or not day.isdigit():
    exit("Invalid data!")

month = input("Enter month (MM): ")
if len(month) != 2 or int(month) < 1 or int(month) > 12 or not month.isdigit():
    exit("Invalid data!")

year = input("Enter year (YYYY): ")
if len(year) != 4 or not year.isdigit():
    exit("Invalid data!")

date1 = datetime.date.fromisoformat(str(year+ "-"+ month+ "-"+ day))
difference = date2 - date1

print("Days between today and your bithday: "+str(difference.days))