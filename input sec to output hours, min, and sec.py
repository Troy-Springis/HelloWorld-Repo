#input sec to output days, hours, min, and sec.
print("enter a number of seconds between 0 and 86399.")
totalSec = int(input())
totalmin = totalSec//60
sec = totalSec%60
totalhour = totalmin//60
min1 = totalhour%60

print(totalhour, "hours,", min1, "minutes, and", sec,"seconds")
