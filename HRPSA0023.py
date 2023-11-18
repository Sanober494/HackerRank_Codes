#Solution for "Birthday Cake Candles" 
#Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure



def birthdayCakeCandles(candles):
    max=candles[0]
    count=0
    for i in range(0,len(candles)):
        if (candles[i]>max):
            max=candles[i]
    for j in range(0,len(candles)):
        if (max==candles[j]):
            count+=1
    print(count)
        

n1=int(input())
n=input()
a1=list(map(int,n.split()))
birthdayCakeCandles(a1)
