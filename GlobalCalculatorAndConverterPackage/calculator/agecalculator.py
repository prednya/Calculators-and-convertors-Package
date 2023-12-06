from datetime import date

def age(day,month,year):
    today = date.today()
    age = int(today.year) - int(year) - int((today.month, today.day) < (month, day))
    return age
