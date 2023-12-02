#Solution for "Simple Array Sum" 
#Link: https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def simpleArraySum(ar):
    sum1=0
    for i in range(0,len(ar)):
        sum1+=ar[i]
    print (sum1)



n=int(input())
num=input()
Arr=list(map(int,num.split()))

simpleArraySum(Arr)
