print("how many seconds have passed since january 1st 2022?")
totalsec= int(input())

#convertions
totalmin = totalsec//60
sec = totalsec%60
totalhour = totalmin//60
min1 = totalhour%60
hour= totalhour%24
day= totalhour//24

#calc estamait population
b= int(334205119)
m= (1/7)-(1/13)+(1/35)
x= totalsec
y=int(m*x+b)
pop = int(y-b)
#put together and display
print("it has been", day, "days,", hour, "hours,", min1, "minutes, and", sec,"seconds since jan 1st 2022. in that time the population has increased by", pop)
print("making the estimated population", y)
