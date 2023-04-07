# Code author: Dagaraliyev Asliddinbek.

from datetime import date

def todays_date():
    present_day = ""
    today = date.today()
    days = today.day
    present_day += f"{days}-"
    if today.month == 1:
        month = "Yanvar"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 2:
        month = "Fevral"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 3:
        month = "Mart"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 4:
        month = "Aprel"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 5:
        month = "May"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 6:
        month = "Iyun"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 7:
        month = "Iyul"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 8:
        month = "Avgust"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 9:
        month = "Sentabr"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 10:
        month = "Oktabr"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 11:
        month = "Noyabr"
        month = str(month)
        present_day += f"{month}, "
    elif today.month == 12:
        month = "Dekabr"
        month = str(month)
        present_day += f"{month}, "
    else:
        False

    year = today.year
    year = str(year)
    present_day += f"{year}-yil"

    return present_day

