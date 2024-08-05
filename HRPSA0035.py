#Solution for "Utopian Tree" 
#Link: https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def utopianTree(n):
    s=1
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    else:
        s = 2
        for i in range(2, (n+1)):
            if (i % 2 == 0):
                s += 1
            else:
                s*=2
        print(s)

n1=int(input())
for j in range(0, n1):
    a1=int(input())
    utopianTree(a1)
