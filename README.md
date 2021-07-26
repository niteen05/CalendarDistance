# A CLI application to calculate the distance in whole days between two dates
<b>Problem Statement<b> <br>
Calculate the distance in whole days between two dates, counting only the days in between those dates, i.e. 01/01/2001 to 03/01/2001 yields “1”. The valid date range is between 01/01/1900 and 31/12/2999, all other dates should be rejected.

## To run locally

1. clone the repository <br>
git clone https://github.com/niteen05/CalendarDistance.git

2. make sure python3 is installed <br>
open terminal and type python3 --version

3. navigate to directory CalenderDistance, run the folowing command. <br>
python3 CalendarDistance.py

4. This executes the program and run few test cases 3 sucess and one failure test cases and waits for user input. <br>

```
niteenacharya@ CalendarDistance % python3 CalendarDistance.py
Test case passed
Test case passed
Test case passed
Test with data failed:[ 3/1/1989 , 3/8/1983 ] Actual: 1979 Expected: 2036
Welcome to Calendar Distance Program.
 invalid date will exit the program
Enter the from date in dd/mm/yyyy format:12/12/2021
Enter the to date in dd/mm/yyyy format:15/12/2021
Both dates are valid
Distance between following dates:[ 12/12/2021 , 15/12/2021 ] is: 2
Enter the from date in dd/mm/yyyy format:25/11/2021
Enter the to date in dd/mm/yyyy format:25/10/2021
Both dates are valid
Distance between following dates:[ 25/11/2021 , 25/10/2021 ] is: 30
Enter the from date in dd/mm/yyyy format:20/10/1988
Enter the to date in dd/mm/yyyy format:20/10/2008
Both dates are valid
Distance between following dates:[ 20/10/1988 , 20/10/2008 ] is: 7304
Enter the from date in dd/mm/yyyy format:25/25/2000
entered month is invalid. [month range: 1-12]
niteenacharya@ CalendarDistance % 
```

## Above program is tested against following test data

```
test_cases = [('2/6/1983', '22/6/1983', 19, 'P'), 
              ('4/7/1984', '25/12/1984', 173, 'P'),
              ('3/1/1989', '3/8/1983', 2036, 'F'),
              ('3/1/1989', '3/8/1983', 2036, 'P')]
```

## Details about code
Code has 5 functions.
1. isValidDate(aDate): <br>
This function validates user input. invalid input exit the program.

2. isLeapYear(year): <br>
This function checks for leap year.

3. calculateDistance(year1, month1, day1): <br>
This function increment date by one day each time it is called. This changes month, year accordingly. 

4. distanceBetweenDates(d1, m1, y1, d2, m2, y2): <br>
This function call other function calculateDistance and add one count to days. 

5. test(): <br>
This block is to test code. 

## TODO
1. Currently there is no proper exit condition. 
2. Program exits abruptly for invalid input.

## Conclusion
Any further questions, check with the author[niteen].