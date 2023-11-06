#Solution for "Divisible Sum Pairs" 
#Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

#Problem Solving-> Algorithms-> Data Structures


def divisibleSumPairs(n, k, ar):
    c=0
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if (((ar[i]+ar[j])%k)==0):
                c+=1
    print(c)
    
num=input()
Num=list(map(int,num.split()))
arr=input()
Arr=list(map(int,arr.split()))
divisibleSumPairs(Num[0],Num[1],Arr)

