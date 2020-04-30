day=int(input('Enter a day:'))
month=int(input('Enter a month:'))
year=int(input('Enter a year:'))
d=[31,30,31,30,31,30,31,30,31,30,31,30]
d_passed=0


for i in d[:month-1]:
       d_passed=d_passed+i


d_passed=d_passed+day



if (year%4 == 0) or (year%4 == 0 and year%100 != 0):
    d_passed=d_passed-1
    
    
print("day passed:",d_passed)
