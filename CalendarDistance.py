#CalendarDistance.py
import sys
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def calculateDistance(year1, month1, day1):
    if month1 ==2:
        if isLeapYear(year1):
            if day1 < daysOfMonths[month1-1]+1:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
        else: 
            if day1 < daysOfMonths[month1-1]:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
    else:
        if day1 < daysOfMonths[month1-1]:
             return year1, month1, day1+1
        else:
            if month1 ==12:
                return year1+1,1,1
            else:
                    return year1, month1 +1 , 1

def distanceBetweenDates(d1, m1, y1, d2, m2, y2):
    if (y1 > y2):
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    elif (y1==y2 and m1>m2):
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    elif (m1==m2 and d1>d2):
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
        
    days=-1
    while(not(m1==m2 and y1==y2 and d1==d2)):
        y1,m1,d1 = calculateDistance(y1,m1,d1)
        days+=1
    return days

# Test
def test():
    test_cases = [('2/6/1983', '22/6/1983', 19, 'P'), 
                  ('4/7/1984', '25/12/1984', 173, 'P'),
                  ('3/1/1989', '3/8/1983', 2036, 'F'),
                  ('3/1/1989', '3/8/1983', 2036, 'P')]
    for (dt1, dt2, answer, expected) in test_cases:
        #dt1,dt2 = args.split(',')
        isValidDate(dt1)
        isValidDate(dt2)
        d1,m1,y1 = dt1.split('/')
        d2,m2,y2 = dt2.split('/')
        result = distanceBetweenDates(int(d1), int(m1), int(y1), int(d2), int(m2), int(y2))
        if (result != answer and expected == 'P'):
            print ("Test with data failed:[",dt1,",",dt2,"] Actual:", result, "Expected:",answer)
        else:
            print ("Test case passed")
test()
print("Welcome to Calendar Distance Program.\n invalid date will exit the program")

while(True):
    fromDate = input ("Enter the from date in dd/mm/yyyy format:")
    isValidDate(fromDate)
    d1,m1,y1 = fromDate.split('/')
    toDate = input ("Enter the to date in dd/mm/yyyy format:")
    isValidDate(toDate)
    d2,m2,y2 = toDate.split('/')
    print("Both dates are valid")
    result = distanceBetweenDates(int(d1), int(m1), int(y1), int(d2), int(m2), int(y2))
    print ("Distance between following dates:[",fromDate,",",toDate,"] is:", result)