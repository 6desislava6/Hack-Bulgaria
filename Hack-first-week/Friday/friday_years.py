import calendar


def friday_years(start_year, end_year):
    overall_friday_years = 0
    for year in range(start_year, end_year):
        fridays_in_year = 0
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            for week in month_calendar:
                if week[4] != 0:
                    fridays_in_year += 1
        if fridays_in_year == 53:
            overall_friday_years += 1
    return overall_friday_years

print(friday_years(1000, 2000))
print(friday_years(1753, 2000))
print(friday_years(1990, 2015))
print(friday_years(1500, 2000))
print(friday_years(1000, 1500))
