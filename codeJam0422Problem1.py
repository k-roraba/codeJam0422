# codeJam 2022 Quals
# punched cards problem
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

# original produced runtime error, cause unknown.   
# changing the output array to store every solution (rather than every line) as a value 
# got it to pass.  Maybe in the old method I was using up too much memory.


# the analysis section recommends nested for loops, but it uses a modulo check to decide which char to 
# print at which position.  Same time complexity, but I wonder which operation 
# (checking position, or running through the loop my way) is more efficient.
# definitely didn't think of checking position.

case = int(input())
output = []

#get parameters, create output
for i in range(case):
    output.append("Case #")
    output[i] = output[i] + str(i+1) + ":\n"
    r, c = [int(x) for x in input().split()]

    #row 0
    output[i] += "..+"
    for j in range(c-1):
        output[i] += "-+"
    
    output[i] += "\n"
    
    #row 1
    output[i] += "..|"
    for j in range(c-1):
        output[i] += ".|"
        
    output[i] += "\n"
    
    #rows 2 - 2*r
    for k in range(r-1):
        output[i] += "+"
        for l in range(c):
            output[i] += "-+"
        output[i] += "\n|"
        for l in range(c):
            output[i] += ".|"
        output[i] += "\n"
    
    output[i]+= "+"    
    #row last
    for k in range(c):
        output[i] += "-+"
    
    
#print output
for i in range(case):
    print(output[i])
