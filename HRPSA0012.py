#Solution for "Breaking the Records" 
#Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def breakingRecords(scores):
    Max=scores[0]
    Min=scores[0]
    High=0
    Low=0
    for i in range(0,len(scores)):
        if (scores[i]>Max):
            Max=scores[i]
            High+=1
        if (scores[i]<Min):
            Min=scores[i]
            Low+=1
    print(High,Low)

n=int(input())
arr=input()
Arr=list(map(int,arr.split()))
breakingRecords(Arr)

