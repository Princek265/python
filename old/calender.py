import calendar

# Input date in MM DD YYYY format
date_input = input("Enter the date (MM DD YYYY): ")
month, day, year = map(int, date_input.split())

# Get the day of the week as an integer (0 is Monday, 6 is Sunday)
day_of_week = calendar.weekday(year, month, day)

# List of day names
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# Get the name of the day
day_name = days[day_of_week]

print(day_name)
