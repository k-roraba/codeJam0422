#  CodeJam 2022 Quals Problem 3
#  dice rolls
#  https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

# this worked for the first test set, but exceeded the time limit on the second
# I think I should sort and fiddle with the dice during intake
# instead of having one pass for intake, another for sorting, and another for actually analysing...

# will come back to it

def bubblesort(elements):
# Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
	            #swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

def removeBad(elements, counter, start):
    if counter >= len(elements):
        return
    for n in range(start, len(elements)):
        if(elements[n] <= n):
            elements.remove(elements[n])
            start = n
            break

    removeBad(elements, counter+1, start)

                     
case = int(input())
output = []

for i in range(case):
    output.append(0)
    n = int(input())
    dice = []
    vals = [int(x) for x in input().split()]
    for j in range(n):
        dice.append(vals[j])

    bubblesort(dice)
    removeBad(dice, 0, 0)

    for j in range(len(dice)):
        if(dice[j] > j):
            output[i] += 1
        else:
            break


            
        
for i in range(case):
    print("Case #{}:".format(i+1), output[i])

#this worked!!!
        

