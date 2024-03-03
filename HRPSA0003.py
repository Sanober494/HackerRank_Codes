#Solution for "Compare the triplets" 
#Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def compareTriplets(a, b):
    c1=0
    c2=0
    points=[]
    for i in range(0,3):
        if (a[i]>b[i]):
            c1+=1
        elif (b[i]>a[i]):
            c2+=1
        else:
            continue
    points.append(c1)
    points.append(c2)
    return (points)         
   
a1=input()
A1=list(map(int,a1.split()))
b1=input()
B1=list(map(int,b1.split()))
l=compareTriplets(A1,B1)

for j in range(0,2):
    print(l[j], end=" ")

