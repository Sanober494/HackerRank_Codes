#Solution for "Apple Orange"
#Link: https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def countApplesAndOranges(s, t, a, b, apples, oranges):
    new_apples=[]
    new_oranges=[]
    apple_count=0
    orange_count=0
    for i in range(0,len(apples)):
        l=apples[i]+a
        new_apples.append(l)
    for j in range(0,len(oranges)):
        e=oranges[j]+b
        new_oranges.append(e)
    for k in range(0,len(new_apples)):
        if (new_apples[k]>=s and new_apples[k]<=t):
            apple_count+=1
    for l in range(0,len(new_oranges)):
        if (new_oranges[l]>=s and new_oranges[l]<=t):
            orange_count+=1
    print(apple_count)
    print(orange_count)
        
s1=input()
Arr=list(map(int,s1.split()))
S=Arr[0]
T=Arr[1]
a1=input()
Arr1=list(map(int,a1.split()))
A=Arr1[0]
B=Arr1[1]
b1=input()
Arr2=list(map(int,b1.split()))
M=Arr2[0]
N=Arr2[1]
m_values=input()
Arr3=list(map(int,m_values.split()))
n_values=input()
Arr4=list(map(int,n_values.split()))
countApplesAndOranges(S, T, A, B, Arr3, Arr4)
