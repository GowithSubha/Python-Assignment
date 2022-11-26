# write a program to take a list of 10 numbers and stored even position number in a list and display it.
thislist=[5,6,9,7,25,42,73,82,94,21]
Ep=[]
Op=[]
for i in range(len(thislist)):
    if i%2!=0:
        Ep.append(thislist[i])
    else:
        Op.append(thislist[i])
        
        
print("The even position numbers are: ", Ep)
print("The odd position numbers are: ", Op)