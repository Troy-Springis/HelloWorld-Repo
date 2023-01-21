#input population, output flapjack consumption
print("what is the population?")
pop= int(input())

#math
flap= int((((((pop+305)**2)-12)/50)**(1/5)))

#print result
print(flap, "flapjacks were eaten when the population was", pop)
