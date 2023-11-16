#Solution for "A Very Big Sum" 
#Link: https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def aVeryBigSum(ar):
    ans=sum(ar)
    return (ans)

n=int(input())
a1=input()
A1=list(map(int,a1.split()))
print(aVeryBigSum(A1))
