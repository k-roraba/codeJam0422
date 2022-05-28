# codeJam 2022 Quals
# punched cards problem
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

# produced runtime error

case = int(input())
output = []

#get parameters, create output
for i in range(case):
    r, c = [int(x) for x in input().split()]
    #row 0
    output.append("..+")
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
    print("Case #{}:".format(i+1))
    print(output[i])
    
