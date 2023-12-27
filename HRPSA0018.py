#Solution for "Beautiful Days at the Movies" 
#Link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def beautifulDays(i, j, k):
    count=0
    for m in range(i,(j+1)):
        
        l=str(m)[::-1]
        L=int(l)
        beautyNum=abs(m-L)
        if beautyNum%k==0:
            count+=1
    print(count)
            
numbers=input()
Num=list(map(int,numbers.split()))
beautifulDays(Num[0],Num[1],Num[2])
