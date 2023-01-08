# exercise 4.4 from unit 4
'''
You must write a program that knows how to generate dates and times from a certain date to infinity. You will write the plan step by step until you reach a complete plan. Follow the instructions in the following sections.

Write a function called gen_secs that returns a generator that produces all possible seconds ranges (numbers between 0 and 59).

def gen_secs():
Write a function called gen_minutes that returns a generator that produces all possible minute ranges (numbers between 0 and 59).

def gen_minutes():
Write a function called gen_hours that returns a generator that produces all possible hour ranges (numbers between 0 and 23).

def gen_hours():
Realize a generator function called gen_time.
The generator must generate all possible hours of the day starting at 00:00:00.
The generator function must use the gen_secs, gen_minutes, and gen_hours generators to print the time in the following format: 01:23:45.

Guidelines:

You can use the following format for the printing operation - "%02d:%02d:%02d" (string format).
Check that the generator function you wrote works using a for loop that will print the following time each time:

To view an accessible code snippet
for gt in gen_time():
    print(gt)
Note: The output is partial of course.

Write a generator function named gen_years defined as follows:

def gen_years(start=2019):
    #<yield>
The generator function receives as a parameter a number representing a year (with a default value of the current year), and produces the year received as a parameter and all the years from it onwards.

Write a function called gen_months defined as follows:

def gen_months():
The function returns a generator that produces all the numbers of the months of the year (numbers in the range 1 to 12).

Write a function called gen_days defined as follows:

def gen_days(month, leap_year=True):
The function accepts as parameters an integer representing a month number and a Boolean variable representing whether it is a leap year or not.

The function returns a generator that produces the number of days in that month (depending on the month and the data regarding a leap year or not).

You can use the following sources, for the number of days in each month and leap years:

It's time to combine all the code we've written so far!

Write a generator function named gen_date defined as follows:

def gen_date():
    #<yield>
The generator returned from the function must produce a complete date signature, in the following format:

dd/mm/yyyy hh:mm:ss.

For the purpose of the task, of course you must use the generators you have already created. Remember to check whether a year is a leap year or not.

Below is an example of a partial run (which includes printing the values ​​extracted from the generator):

01/01/2019 00:00:00
01/01/2019 00:00:01
01/01/2019 00:00:02

Call the next function in a loop for the generator object that is returned from the gen_date generator function and print the value produced from the generator after every 1000000 iterations.

Below is a sample run:

12/01/2019 13:46:40
24/01/2019 03:33:20
04/02/2019 17:20:00
Note: The output is of course partial (this is just the beginning of it).

'''
from datetime import date, datetime

current_year = datetime.now().year

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def gen_secs():
    sec = -1
    while sec < 59:
        sec += 1
        yield sec

def gen_minutes():
    minute = -1
    while minute < 59:
        minute += 1
        yield minute

def gen_hours():
    hour = -1
    while hour < 23:
        hour += 1
        yield hour

def gen_years(start=current_year):
    start -= 1
    while start < datetime.now().year:
        start += 1
        yield start
        
def gen_month():
    month = 0
    while month < 12:
        month += 1
        yield month

def gen_days(month, leap_year=True):
    days = 0
    if month in [4, 6, 9, 11]:
        days = 30

    elif month == [1, 3, 5, 7, 8, 10, 12]:
        days = 31

    elif month == 2 and leap_year:
        days = 29

    elif month == 2 and not leap_year:
        days = 28

    return (day for day in range(1, days + 1))
  
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                dt = datetime(2020, 12, 27, hour, minute, sec)
                yield dt.strftime("%H:%M:%S")
                
def gen_date():
    for year in gen_years():
        for month in gen_month():
            for day in gen_days(month, is_leap_year(year)):
                dt = datetime(year, month, day)
                yield dt.strftime("%m/%d/%Y")

def gen_date_time():
    for date in gen_date():
        for time in gen_time():
            yield f'{date} {time}'

def main():
    g = gen_date_time()
    for _ in range(0, 10000000, 1000000):
        print(next(g))

if __name__ == "__main__":
    main()
