# codeJam 2022 Quals Problem 2
# 3D printing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b

# this worked

case = int(input())
output = []


for i in range(case):
    want = 1000000
    c, m, y, k = 10000000, 10000000, 10000000, 10000000 
    for j in range(3):
        vals = [int(x) for x in input().split()]
        c = vals[0] if vals[0] < c else c
        m = vals[1] if vals[1] < m else m
        y = vals[2] if vals[2] < y else y
        k = vals[3] if vals[3] < k else k
    
    if(c >= want):
        c, m, y, k = want, 0, 0, 0
        output.append(str(c))
        output[i] += " " + str(m) + " "
        output[i] += str(y) + " "
        output[i] += str(k)
    else:
        want -= c
        if(m >= want):
            m, y, k = want, 0, 0
            output.append(str(c))
            output[i] += " " + str(m) + " "
            output[i] += str(y) + " "
            output[i] += str(k)
        else:
            want -= m

            if(y >= want):
                y, k = want, 0
                output.append(str(c))
                output[i] += " " + str(m) + " "
                output[i] += str(y) + " "
                output[i] += str(k)
            else:
                want -= y
                if(k >= want):
                    k = want
                    output.append(str(c))
                    output[i] += " " + str(m) + " "
                    output[i] += str(y) + " "
                    output[i] += str(k)
                else:
                    output.append("IMPOSSIBLE")

for i in range(case):
    print("Case #{}:".format(i+1), output[i])



