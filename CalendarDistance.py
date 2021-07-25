#CalendarDistance.py
import sys

def isValidDate(aDate):
    day,month,year = aDate.split('/')
    day=int(day)
    month=int(month)
    year=int(year)
    
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        max_days=31
    elif (month==4 or month==6 or month==9 or month==11):
        max_days=30
    elif (year%4==0 and year%100!=0 or year%400==0):
        max_days=29
    else:
        max_days=28

    if (day<1 or day > max_days):
        sys.exit("entered day is invalid. [day range: 1-28/29/30/31 depending on the month,year]")
    elif (month<1 or month>12):
        sys.exit("entered month is invalid. [month range: 1-12]")
        
    elif (year<1900 or year>2999):
        sys.exit("entered year is invalid. [year range: 1900-2999]")
        
fromDate = input ("Enter the from date in dd/mm/yyyy format:")
isValidDate(fromDate)
toDate = input ("Enter the to date in dd/mm/yyyy format:")
isValidDate(toDate)
print("Both dates are valid")
