#Solution for "Diagonal Difference" 
#Link: https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure

def diagonalDifference(arr):
    priSum=0
    secSum=0
    for i in range(0,n):
        priSum+=arr[i][i]
    for j in range(0,n):
        secSum+=arr[j][n-1-j]
    newSum=priSum-secSum    
    return abs(newSum)
       
n=int(input())
matrix=[]
for i in range(0,n):
    a1=input()  
    A1=list(map(int,a1.split()))
    matrix.append(A1)
print(diagonalDifference(matrix))
        
