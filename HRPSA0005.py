#Solution for "Plus Minus" 
#Link: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def plusMinus(arr):
    Pos=0
    Neg=0
    Zero=0
    for j in range(0,len(arr)):
        if (arr[j]>0):
            Pos+=1
        elif (arr[j]<0):
            Neg+=1
        else:
            Zero+=1
    print(round(Pos/n,6))
    print(round(Neg/n,6))
    print(round(Zero/n,6))
    
Arr=[]
n=int(input())
a1=input()

Arr=list(map(int,a1.split()))
plusMinus(Arr)
