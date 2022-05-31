#  CodeJam 2022 Quals Problem 3
#  dice rolls
#  https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

# this is a leaner version; it passes test set 1, but gets the wrong answer on test set 2...?

# incidentally, the Google solution has something closer to my original solution:
# one pass to sort, then a linear loop to determine the length straight.
# They were more insightful with their counting method, though.
                     
case = int(input())
output = []

for i in range(case):
    output.append("Case #")

    n = int(input())
    dice = []
    vals = [int(x) for x in input().split()]

    dice.append(vals[0])
    ans = 1

    for j in range(n - 1):
        for k in range(len(dice)):
            if vals[j+1] < dice[k]:
                dice.insert(k, vals[j+1])
                if dice[k] > k+1:
                    ans += 1
                break
        
        if vals[j+1] >= dice[len(dice)-1]:
            dice.append(vals[j+1])
            if dice[k] > k+1:
                ans += 1

    output[i] = output[i] + str(i+1) + ": " + str(ans)
        
for i in range(case):
    print(output[i])

        



