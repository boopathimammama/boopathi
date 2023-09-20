def isLeap Year(year):

if (year & 4 = @ and year 180 != 0) or year $ 400 = 0:

return True

else:

return False

year = int(input("Enter a year : "))

if isLeapYear (year):

print('{} is a leap year.'.format(year))

else:

print('{} is not a leap year.'.format(year))
