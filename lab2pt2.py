print("how many days has it been since jan 1st 2022?")
day = int(input())
print("how many hours has it been since the day started?")
hour = int(input())
print("how many minutes has it been since the hour started?")
min1= int(input())
print("how many seconds has it been sice the minute started")
sec= int(input())

#convert all to find total seconds
totalsec= (day*24*60*60)+(hour*60*60)+(min1*60)+sec

#y=mx+b, y:estimated population, m: , x: input, b:starting population
b= int(334205119)
m= (1/7)-(1/13)+(1/35)
x= totalsec
y=int(m*x+b)
print("the estimated population would be", y)
