#Solution for "Staircase" 
#Link: https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure

def staircase(n):
    space= " "
    hashes="#"    
    for i in range(1,n+1):
        print(space*(n-i), end="")
        print(hashes*i)      
        
        
n1=int(input())
staircase(n1)
